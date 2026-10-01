"""Focused checks for file safety and native-package layout; no device writes."""

import importlib.util
import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("modpod", SOURCE_ROOT / "tools" / "modpod.py")
modpod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modpod)


class ThemeToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.old_root = modpod.ROOT
        modpod.ROOT = self.root
        shutil.copytree(SOURCE_ROOT / "themes", self.root / "themes")
        shutil.copytree(SOURCE_ROOT / "templates", self.root / "templates")

    def tearDown(self):
        modpod.ROOT = self.old_root
        self.temp.cleanup()

    def test_rejects_traversal_and_config_injection(self):
        for slug in ("../outside", "/tmp/outside", "a/b", "UPPER", "bad\nname", "a" * 49):
            with self.subTest(slug=slug), self.assertRaises(ValueError):
                modpod.new_theme(slug, "paper")
        path = self.root / "themes" / "paper" / "theme.json"
        theme = json.loads(path.read_text())
        theme["name"] = "Injected\nsbs: /.rockbox/wps/other.sbs"
        path.write_text(json.dumps(theme))
        with self.assertRaises(ValueError):
            modpod.load_theme("paper")

    def test_new_theme_preserves_original_and_refuses_overwrite(self):
        source = (self.root / "themes" / "paper" / "theme.json").read_bytes()
        modpod.new_theme("my-theme", "paper")
        self.assertEqual(modpod.load_theme("my-theme")["slug"], "my-theme")
        with self.assertRaises(ValueError):
            modpod.new_theme("my-theme", "midnight")
        self.assertEqual((self.root / "themes" / "paper" / "theme.json").read_bytes(), source)

    def test_package_has_only_expected_native_files(self):
        path = modpod.package_theme(modpod.load_theme("paper"))
        first = path.read_bytes()
        with zipfile.ZipFile(path) as archive:
            self.assertEqual(set(archive.namelist()), {
                ".rockbox/themes/paper.cfg", ".rockbox/wps/paper.wps", ".rockbox/wps/paper.sbs"
            })
            config = archive.read(".rockbox/themes/paper.cfg").decode()
            self.assertIn("wps: /.rockbox/wps/paper.wps", config)
            self.assertNotIn("$", config)
        modpod.package_theme(modpod.load_theme("paper"))
        self.assertEqual(path.read_bytes(), first)

    def test_output_symlink_cannot_leave_repository(self):
        with tempfile.TemporaryDirectory() as other:
            (self.root / "dist").symlink_to(other, target_is_directory=True)
            with self.assertRaises(ValueError):
                modpod.package_theme(modpod.load_theme("paper"))
            self.assertEqual(list(Path(other).iterdir()), [])

    def test_native_variants_keep_templates_and_assets(self):
        modpod.new_theme("piplupos-pink", "piplupos")
        archive_path = modpod.package_theme(modpod.load_theme("piplupos-pink"))
        with zipfile.ZipFile(archive_path) as archive:
            self.assertIn(".rockbox/wps/piplupos-pink/piplup.bmp", archive.namelist())
            self.assertIn(".rockbox/wps/piplupos-pink/water.bmp", archive.namelist())
            self.assertIn(".rockbox/fonts/14-Adobe-Helvetica-Bold.fnt", archive.namelist())
            self.assertTrue(archive.read(".rockbox/fonts/14-Adobe-Helvetica-Bold.fnt").startswith(b"RB12"))
            self.assertIn(".rockbox/fonts/Adobe-Helvetica-LICENSE.txt", archive.namelist())
            wps = archive.read(".rockbox/wps/piplupos-pink.wps").decode()
            self.assertIn("%xd(pa)", wps)
            self.assertEqual(archive.read(".rockbox/wps/piplupos-pink/piplup.bmp"),
                             (self.root / "themes/piplupos/assets/piplup.bmp").read_bytes())
            config = archive.read(".rockbox/themes/piplupos-pink.cfg").decode()
            self.assertIn("piplupos-pink.wps", config)

    def test_invalid_and_symlink_fonts_are_rejected(self):
        source = self.root / "themes/paper/fonts"
        source.mkdir()
        font = source / "bad.fnt"
        font.write_bytes(b"not a Rockbox font")
        with self.assertRaises(ValueError):
            modpod.package_theme(modpod.load_theme("paper"))
        font.unlink()
        font.symlink_to(self.root / "templates/ipodvideo/theme.cfg.in")
        with self.assertRaises(ValueError):
            modpod.new_theme("unsafe-font", "paper")
        self.assertFalse((self.root / "themes/unsafe-font").exists())

    def test_symlink_assets_are_rejected_before_variant_is_created(self):
        source = self.root / "themes/paper/assets"
        source.mkdir()
        (source / "outside.bmp").symlink_to(self.root / "templates/ipodvideo/theme.cfg.in")
        with self.assertRaises(ValueError):
            modpod.new_theme("unsafe-variant", "paper")
        self.assertFalse((self.root / "themes/unsafe-variant").exists())
        with self.assertRaises(ValueError):
            modpod.package_theme(modpod.load_theme("paper"))

    def test_rejects_bad_palette_and_wrong_device(self):
        path = self.root / "themes" / "paper" / "theme.json"
        base = json.loads(path.read_text())
        for update in ({"colors": {**base["colors"], "accent": "#BADHEX"}}, {"target": "ipod6g"}):
            path.write_text(json.dumps({**base, **update}))
            with self.assertRaises(ValueError):
                modpod.load_theme("paper")


if __name__ == "__main__":
    unittest.main()
