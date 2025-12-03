@echo off
echo 제임스돈 아이디 관리 통합 프로그램 실행 중...
python main.py
if errorlevel 1 (
    echo.
    echo 오류 발생! Python이 설치되어 있는지 확인하세요.
    pause
)

