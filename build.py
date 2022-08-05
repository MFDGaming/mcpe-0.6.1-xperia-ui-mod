from sdk import Patch, Mod
from os import getcwd, sep

mod = Mod()
patches = [
    Patch(0xcd030, b"\x00\x20\x00\xbf"), # movs r0, #0 nop
    # Minecraft::_reloadInput()
    Patch(0xce3c0, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # Button::hovered(Minecraft*, int, int)
    Patch(0xd0a4c, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # Screen::updateTabButtonSelection()
    Patch(0xdacd4, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    Patch(0xdb0d2, (
        b"\x5f\xf4\xe8\x70" +
        b"\x9a\xf0\x6d\xfd" +
        b"\x04\x46" +
        b"\x09\xf0\x58\xfd" +
        b"\xff\xd9"
    )),
    # GameRenderer::pick(float)
    Patch(0xf2ce2, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # GameRenderer::renderLevel(float)
    Patch(0xf3bae, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # Options::update(std::vector<std::string, std::allocator<std::string> >&)
    Patch(0xcf4ee, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
    # Gui::render(float, bool, int, int)
    Patch(0xd90f2, b"\x01\x20\x00\xbf"), # movs r0, #1 nop
]

for patch in patches:
    mod.add_patch(patch)

mod.save(getcwd() + sep + "xperia_ui.mod")

