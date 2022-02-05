#
# create by kangprog
#
import time

from tkinter import *
from consts.const import (
    APP_COLOR,
    TITLE_NAME,
    RESOULTION,
    FONT, FONT_SIZE, BUTTON_FONT_SIZE,
    METEO, WARRENT,
    BLACK_MAGITION_3RD_METEO_SECOND,
    BLACK_MAGITION_3RD_WARRENT_SECOND,
    RESET,
    ALL_RESET,
    ALL_START,
)


def init_label():
    #
    # 사용되는 그리드
    # (0,0) (0,1), (1,0), (1,1)
    #

    meteo_label = Label(
        root,
        text= METEO,
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    meteo_label.grid(
        row=0,
        column=0,
    )

    seperate_label_row0 = Label(
        root,
        width=0,
        text= ':',
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    seperate_label_row0.grid(
        row=0,
        column=1,
    )

    warrent_label = Label(
        root,
        text= WARRENT,
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    warrent_label.grid(
        row=1,
        column=0,
        sticky=W
    )

    seperate_label_row1 = Label(
        root,
        width=0,
        text= ':',
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    seperate_label_row1.grid(
        row=1,
        column=1,
    )


def init_pattern_time():
    #
    # 사용되는 그리드
    # (0,2) (1,2)
    #

    BLACK_MAGITION_3RD_METEO = StringVar()
    BLACK_MAGITION_3RD_WARRENT = StringVar()

    BLACK_MAGITION_3RD_METEO.set(BLACK_MAGITION_3RD_METEO_SECOND)
    BLACK_MAGITION_3RD_WARRENT.set(BLACK_MAGITION_3RD_WARRENT_SECOND)

    meteo_second_entry= Entry(
        root,
        width=4,
        background=APP_COLOR,
        borderwidth=0,        
        font=(FONT, FONT_SIZE, ""),
        textvariable=BLACK_MAGITION_3RD_METEO
    )
    meteo_second_entry.grid(
        row=0,
        column=2,
    )

    warrent_second_entry= Entry(
        root,
        width=4,
        background=APP_COLOR,
        borderwidth=0,
        font=(FONT, FONT_SIZE, ""),
        textvariable=BLACK_MAGITION_3RD_WARRENT
    )
    warrent_second_entry.grid(
        row=1,
        column=2,
    )


def init_button():
    meteo_reset_button = Button(
        text=RESET,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, "")
    )
    meteo_reset_button.grid(
        row=0,
        column=3
    )

    warrent_reset_button = Button(
        text=RESET,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, "")
    )
    warrent_reset_button.grid(
        row=1,
        column=3
    )

    all_reset_button = Button(
        text=ALL_RESET,
        height=5,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, "")
    )
    all_reset_button.grid(
        row=0,
        column=4,
        rowspan=2
    )

    all_start = Button(
        text=ALL_START,
        height=5,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, "")
    )
    all_start.grid(
        row=0,
        column=5,
        rowspan=2
    )


if __name__ == "__main__":
    root = Tk()

    root.geometry(RESOULTION)
    root.title(TITLE_NAME)
    root.configure(bg=APP_COLOR)

    _ = init_label()
    _ = init_pattern_time()
    _ = init_button()

    root.mainloop()


