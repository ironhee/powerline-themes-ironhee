green = 193
dark_pink = 9
dark_white = 15
white = 249
whiter = 254
dark_black = 0
light_grey = 238

class Color(DefaultColor):
    USERNAME_FG = 8
    USERNAME_BG = 251
    USERNAME_ROOT_BG = 209

    HOSTNAME_FG = 8
    HOSTNAME_BG = 7

    HOME_SPECIAL_DISPLAY = True
    HOME_BG = green
    HOME_FG = dark_black
    PATH_BG = light_grey
    PATH_FG = white
    CWD_FG = green
    SEPARATOR_FG = whiter

    READONLY_BG = 209
    READONLY_FG = 15

    REPO_CLEAN_BG = dark_black
    REPO_CLEAN_FG = white
    REPO_DIRTY_BG = dark_black
    REPO_DIRTY_FG = green

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = green
    CMD_PASSED_FG = dark_black
    CMD_FAILED_BG = 9
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 150
    VIRTUAL_ENV_FG = 0
