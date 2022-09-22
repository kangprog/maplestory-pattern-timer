#
# create by kangprog
#
import time

from functools import partial
from threading import Thread
from tkinter import *
from utils.util import on_click
from consts.const import *


def init_label():
    #
    # 사용되는 그리드
    # (0,0) (0,1), (1,0), (1,1)
    #

    boom_label = Label(
        root,
        text= BOOM,
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    boom_label.grid(
        row=0,
        column=0,
        sticky=W
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

    left_stone_label = Label(
        root,
        text= LEFT_STONE,
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    left_stone_label.grid(
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

    BRASE_30_label = Label(
        root,
        text= BRASE_30,
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    BRASE_30_label.grid(
        row=2,
        column=0,
    )

    seperate_label_row2 = Label(
        root,
        width=0,
        text= ':',
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    seperate_label_row2.grid(
        row=2,
        column=1,
    )

    BRASE_45_label = Label(
        root,
        text= BRASE_45,
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    BRASE_45_label.grid(
        row=3,
        column=0,
    )

    seperate_label_row3 = Label(
        root,
        width=0,
        text= ':',
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    seperate_label_row3.grid(
        row=3,
        column=1,
    )

    BRASE_60_label = Label(
        root,
        text= BRASE_60,
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    BRASE_60_label.grid(
        row=4,
        column=0,
    )

    seperate_label_row4 = Label(
        root,
        width=0,
        text= ':',
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    seperate_label_row4.grid(
        row=4,
        column=1,
    )

    OUT_TIMER_label = Label(
        root,
        text= OUT_TIMER,
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    OUT_TIMER_label.grid(
        row=5,
        column=0,
        sticky=W
    )

    seperate_label_row5 = Label(
        root,
        width=0,
        text= ':',
        bg= APP_COLOR,
        font=(FONT, FONT_SIZE, ""),
    )

    seperate_label_row5.grid(
        row=5,
        column=1,
    )

def init_pattern_time():
    #
    # 사용되는 그리드
    # (0,2) (1,2)
    #

    KALOS_BOOM = StringVar()
    KALOS_LEFT_STONE = StringVar()
    KALOS_BRASE_30 = StringVar()
    KALOS_BRASE_45 = StringVar()
    KALOS_BRASE_60 = StringVar()
    KALOS_OUT_TIMER = StringVar()

    KALOS_BOOM.set(BOOM_SECOND)
    KALOS_LEFT_STONE.set(LEFT_STONE_SECOND)
    KALOS_BRASE_30.set(BRASE_30_SECOND)
    KALOS_BRASE_45.set(BRASE_45_SECOND)
    KALOS_BRASE_60.set(BRASE_60_SECOND)
    KALOS_OUT_TIMER.set(OUT_TIMER_SECOND)

    boom_second_entry= Entry(
        root,
        width=4,
        background=APP_COLOR,
        borderwidth=0,
        font=(FONT, FONT_SIZE, ""),
        textvariable=KALOS_BOOM
    )
    boom_second_entry.grid(
        row=0,
        column=2,
        sticky=E
    )

    left_stone_second_entry= Entry(
        root,
        width=4,
        background=APP_COLOR,
        borderwidth=0,
        font=(FONT, FONT_SIZE, ""),
        textvariable=KALOS_LEFT_STONE
    )
    left_stone_second_entry.grid(
        row=1,
        column=2,
        sticky=W+E
    )

    brase_30_second_entry= Entry(
        root,
        width=4,
        background=APP_COLOR,
        borderwidth=0,
        font=(FONT, FONT_SIZE, ""),
        textvariable=KALOS_BRASE_30
    )
    brase_30_second_entry.grid(
        row=2,
        column=2,
        sticky=W+E
    )

    brase_45_second_entry= Entry(
        root,
        width=4,
        background=APP_COLOR,
        borderwidth=0,
        font=(FONT, FONT_SIZE, ""),
        textvariable=KALOS_BRASE_45
    )
    brase_45_second_entry.grid(
        row=3,
        column=2,
        sticky=W+E
    )

    brase_60_second_entry= Entry(
        root,
        width=4,
        background=APP_COLOR,
        borderwidth=0,
        font=(FONT, FONT_SIZE, ""),
        textvariable=KALOS_BRASE_60
    )
    brase_60_second_entry.grid(
        row=4,
        column=2,
        sticky=W+E
    )

    out_timer_second_entry= Entry(
        root,
        width=4,
        background=APP_COLOR,
        borderwidth=0,
        font=(FONT, FONT_SIZE, ""),
        textvariable=KALOS_OUT_TIMER
    )
    out_timer_second_entry.grid(
        row=5,
        column=2,
        sticky=W+E
    )

    return \
        KALOS_BOOM, boom_second_entry, \
        KALOS_LEFT_STONE, left_stone_second_entry, \
        KALOS_BRASE_30, brase_30_second_entry, \
        KALOS_BRASE_45, brase_45_second_entry, \
        KALOS_BRASE_60, brase_60_second_entry, \
        KALOS_OUT_TIMER, out_timer_second_entry


def init_button(
        root,
        boom_sec, boom_second_entry,
        left_stone_sec, left_stone_second_entry,
        brase_30_sec, brase_30_second_entry,
        brase_45_sec, brase_45_second_entry,
        brase_60_sec, brase_60_second_entry,
        out_timer_sec, out_timer_second_entry
):
    #
    # 사용되는 그리드
    # (0,3), (1,3), (0,4, rowspan=2)
    #

    boom_start_button = Button(
        text=START,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            boom_stringvar=boom_sec,
            boom_sec=BOOM_SECOND,
            boom_second_entry=boom_second_entry
        )
    )
    boom_start_button.grid(
        row=0,
        column=3,
    )

    left_stone_start_button = Button(
        text=START,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            left_stone_stringvar=left_stone_sec,
            left_stone_sec=LEFT_STONE_SECOND,
            left_stone_second_entry=left_stone_second_entry
        )
    )
    left_stone_start_button.grid(
        row=1,
        column=3,
    )

    brase_30_start_button = Button(
        text=START,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            brase_30_stringvar=brase_30_sec,
            brase_30_sec=BRASE_30_SECOND,
            brase_30_second_entry=brase_30_second_entry
        )
    )
    brase_30_start_button.grid(
        row=2,
        column=3,
    )

    brase_45_start_button = Button(
        text=START,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            brase_45_stringvar=brase_45_sec,
            brase_45_sec=BRASE_45_SECOND,
            brase_45_second_entry=brase_45_second_entry
        )
    )
    brase_45_start_button.grid(
        row=3,
        column=3,
    )

    brase_60_start_button = Button(
        text=START,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            brase_60_stringvar=brase_60_sec,
            brase_60_sec=BRASE_60_SECOND,
            brase_60_second_entry=brase_60_second_entry
        )
    )
    brase_60_start_button.grid(
        row=4,
        column=3,
    )

    out_timer_start_button = Button(
        text=START,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            out_timer_stringvar=out_timer_sec,
            out_timer_sec=OUT_TIMER_SECOND,
            out_timer_second_entry=out_timer_second_entry
        )
    )
    out_timer_start_button.grid(
        row=5,
        column=3,
    )


# ==============
    boom_stop_button = Button(
        text=ONE_STOP,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            boom_stringvar=boom_sec,
            boom_sec=BOOM_SECOND,
            boom_second_entry=boom_second_entry,
            check=True,
            button_name = "BOOM"
        )
    )
    boom_stop_button.grid(
        row=0,
        column=4,
    )

    left_stone_stop_button = Button(
        text=ONE_STOP,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            left_stone_stringvar=left_stone_sec,
            left_stone_sec=LEFT_STONE_SECOND,
            left_stone_second_entry=left_stone_second_entry,
            check=True,
            button_name="LEFT_STONE"
        )
    )
    left_stone_stop_button.grid(
        row=1,
        column=4,
    )

    brase_30_stop_button = Button(
        text=ONE_STOP,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            brase_30_stringvar=brase_30_sec,
            brase_30_sec=BRASE_30_SECOND,
            brase_30_second_entry=brase_30_second_entry,
            check=True,
            button_name="BRASE_30"

        )
    )
    brase_30_stop_button.grid(
        row=2,
        column=4,
    )

    brase_45_stop_button = Button(
        text=ONE_STOP,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            brase_45_stringvar=brase_45_sec,
            brase_45_sec=BRASE_45_SECOND,
            brase_45_second_entry=brase_45_second_entry,
            check=True,
            button_name="BRASE_45"
        )
    )
    brase_45_stop_button.grid(
        row=3,
        column=4,
    )

    brase_60_stop_button = Button(
        text=ONE_STOP,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            brase_60_stringvar=brase_60_sec,
            brase_60_sec=BRASE_60_SECOND,
            brase_60_second_entry=brase_60_second_entry,
            check=True,
            button_name="BRASE_60"
        )
    )
    brase_60_stop_button.grid(
        row=4,
        column=4,
    )

    out_timer_stop_button = Button(
        text=ONE_STOP,
        height=2,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            out_timer_stringvar=out_timer_sec,
            out_timer_sec=OUT_TIMER_SECOND,
            out_timer_second_entry=out_timer_second_entry,
            check=True,
            button_name="OUT_TIMER"
        )
    )
    out_timer_stop_button.grid(
        row=5,
        column=4,
    )

    all_reset_button = Button(
        text=ALL_RESET,
        height=5,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            boom_sec, BOOM_SECOND, boom_second_entry,
            left_stone_sec, LEFT_STONE_SECOND, left_stone_second_entry,
            brase_30_sec, BRASE_30_SECOND, brase_30_second_entry,
            brase_45_sec, BRASE_45_SECOND, brase_45_second_entry,
            brase_60_sec, BRASE_60_SECOND, brase_60_second_entry,
            out_timer_sec, OUT_TIMER_SECOND, out_timer_second_entry,
        )
    )
    all_reset_button.grid(
        row=0,
        column=5,
        rowspan=2
    )

    stop_button = Button(
        text=STOP,
        height=5,
        width=15,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
            boom_sec, BOOM_SECOND, boom_second_entry,
            left_stone_sec, LEFT_STONE_SECOND, left_stone_second_entry,
            brase_30_sec, BRASE_30_SECOND, brase_30_second_entry,
            brase_45_sec, BRASE_45_SECOND, brase_45_second_entry,
            brase_60_sec, BRASE_60_SECOND, brase_60_second_entry,
            out_timer_sec, OUT_TIMER_SECOND, out_timer_second_entry,
            all_check=True
        )
    )
    stop_button.grid(
        row=2,
        column=5,
        rowspan=2
    )

    logo_button = Button(
        text = " :) \n made by. 긴옷",
        height=5,
        width=15,
        bg=APP_COLOR,
        font=(FONT, BUTTON_FONT_SIZE, ""),
        command= partial(
            on_click,
            root,
        )
    )
    logo_button.grid(
        row=4,
        column=5,
        rowspan=2
    )


if __name__ == "__main__":
    root = Tk()

    root.geometry(RESOULTION)
    root.title(TITLE_NAME)
    root.configure(bg=APP_COLOR)

    # Label init
    _ = init_label()

    #Pattern Entry init
    boom_sec, boom_second_entry, \
    left_stone_sec, left_stone_second_entry, \
    brase_30_sec, brase_30_second_entry, \
    brase_45_sec, brase_45_second_entry, \
    brase_60_sec, brase_60_second_entry, \
    out_timer_sec, out_timer_second_entry = init_pattern_time()

    # Button Init(with Event)
    _ = init_button(root,
                    boom_sec, boom_second_entry,
                    left_stone_sec, left_stone_second_entry,
                    brase_30_sec, brase_30_second_entry,
                    brase_45_sec, brase_45_second_entry,
                    brase_60_sec, brase_60_second_entry,
                    out_timer_sec, out_timer_second_entry
                    )

    root.mainloop()
