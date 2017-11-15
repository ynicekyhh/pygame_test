# error: 맨 마지막 import 대상은 모듈(*.py) 이어야 한다.
# package(디렉토리)를 import할 수도 있다. (단, package(디렉토리)에 __init__.py가 있어야 한다)
# (__init__이 없더라도 python3.3이상 버전에서 자동으로 넣어주나, python 하위 호환성을 위해 넣어주자)
# 해당 패키지에서 __init__이 존재하는 이유는 외부에 보여줄 애들만 __init__에서 지정할 수 있다.(모듈화)
# import pygame.sound.echo.test_echo

from pygame.sound.echo import test_echo
test_echo()