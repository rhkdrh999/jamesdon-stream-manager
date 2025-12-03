@echo off
echo ========================================
echo 제임스돈 아이디 관리 통합 프로그램 설치
echo ========================================
echo.

echo [1/3] Python 버전 확인...
python --version
if errorlevel 1 (
    echo 오류: Python이 설치되어 있지 않습니다!
    echo https://www.python.org/downloads/ 에서 Python을 설치하세요.
    pause
    exit /b 1
)
echo.

echo [2/3] pip 업그레이드...
python -m pip install --upgrade pip
echo.

echo [3/3] 의존성 설치...
pip install -r requirements.txt
if errorlevel 1 (
    echo 오류: 의존성 설치 실패!
    echo 관리자 권한으로 실행해보세요.
    pause
    exit /b 1
)
echo.

echo ========================================
echo 설치 완료!
echo ========================================
echo.
echo 실행하려면: python main.py
echo.
pause

