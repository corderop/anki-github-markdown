from aqt import gui_hooks
from aqt.editor import Editor

from ... import config
from ...markdown import MarkdownToggler


class EditorButton:
    def enable(self):
        """Enable the editor button to toggle between Markdown and HTML."""
        gui_hooks.editor_did_init_buttons.append(self.__addButton)

    def __addButton(self, buttons: list[str], editor: Editor) -> list[str]:
        button = editor.addButton(
            config.BUTTON_ICON_PATH,
            config.CMD,
            self.__run,
            tip=config.DESCRIPTION,
            keys=config.SHORTCUT,
        )

        buttons.append(button)
        return buttons

    def __run(self, editor: Editor):
        self.editor = editor
        self.field_id = self.editor.currentField

        if self.field_id is None:
            return

        current_html = self.__get_current_field_html()
        modified_html = MarkdownToggler().run(current_html)
        self.__set_current_field_html(modified_html)

    def __get_current_field_html(self) -> str:
        """Get HTML of the active field.

        Returns:
            str: HTML of the active field
        """
        if self.field_id is not None:
            return self.editor.note.fields[self.field_id]

    def __set_current_field_html(self, html: str):
        """Change the HTML content of the current active field.

        Args:
            html (str): HTML to be set in the current active field.
        """
        if self.field_id is not None:
            self.editor.note.fields[self.field_id] = html
            self.editor.set_note(self.editor.note)
