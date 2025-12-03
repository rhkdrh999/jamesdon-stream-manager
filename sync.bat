@echo off
echo ========================================
echo 제임스돈 프로그램 동기화
echo ========================================
echo.

echo [1/2] 최신 버전 가져오기...
git pull origin main
if errorlevel 1 (
    echo.
    echo 경고: Pull 실패 또는 충돌 발생!
    echo git status로 상태를 확인하세요.
    echo.
    pause
)

echo.
echo [2/2] 변경사항 업로드...
git add .
git commit -m "Auto sync: %date% %time%"
git push origin main
if errorlevel 1 (
    echo.
    echo 경고: Push 실패!
    echo 이미 푸시된 내용이거나 충돌이 있을 수 있습니다.
    echo.
    pause
)

echo.
echo ========================================
echo 동기화 완료!
echo ========================================
echo.
pause

