#
# create by kangprog
#
import time

from consts.const import (
    WARRNING_COLOR,
    COMMON_COLOR,
    BLACK_MAGITION_3RD_METEO_SECOND,
    BLACK_MAGITION_3RD_WARRENT_SECOND
)
from utils.thread import THREADING_WITH_TRACE


meteo_pattern = None
warrent_pattern = None


def on_reset(root, stringvar, sec, entry):
    try:
        temp = sec
    except:
        print("[Error] Please input the right value")

    while temp >-1:  
        try:
            if temp < 10:
                stringvar.set("{0:2d}".format(temp))
                entry.configure(fg=WARRNING_COLOR)
            else:
                stringvar.set("{0:2d}".format(temp))
                entry.configure(fg=COMMON_COLOR)
        except Exception as ex:
            print(f"[Error] Set Time Label Error: {ex}")
            break

        root.update()
        time.sleep(1)

        if (temp == 0):
            temp = sec
            
        temp -= 1


def on_click(
        root, 
        meteo_stringvar = None, 
        warrent_stringvar = None, 
        meteo_sec = 0,
        warrent_sec = 0,
        meteo_second_entry = None, 
        warrent_second_entry = None
    ):

    global meteo_pattern, warrent_pattern

    if meteo_sec == BLACK_MAGITION_3RD_METEO_SECOND:
        if meteo_pattern:
            meteo_pattern.kill()
        meteo_pattern = THREADING_WITH_TRACE(
            target=on_reset,
            args=(root, meteo_stringvar, meteo_sec, meteo_second_entry),
        )
        meteo_pattern.start()

    if warrent_sec == BLACK_MAGITION_3RD_WARRENT_SECOND:
        if warrent_pattern:
            warrent_pattern.kill()
        warrent_pattern = THREADING_WITH_TRACE(
            target=on_reset,
            args=(root, warrent_stringvar, warrent_sec, warrent_second_entry),
        )
        warrent_pattern.start()
