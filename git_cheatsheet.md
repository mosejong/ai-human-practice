# Git / GitHub Cheatsheet (완전 한방 복붙용)

## 🔥 기본 흐름 (제일 중요)
```bash
git status
git add .
git commit -m "작업 내용"
git push
```

문제 생기면:
```bash
git pull origin main
git push
```

히스토리 충돌이면:
```bash
git pull origin main --allow-unrelated-histories
```

---

## 🚀 새 프로젝트 시작 (GitHub 연결까지)
```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/아이디/레포이름.git
git push -u origin main
```

---

## 📌 자주 쓰는 명령어
```bash
# 상태 확인
git status

# 전체 파일 추가
git add .

# 특정 파일만 추가
git add 파일명

# 커밋
git commit -m "메시지"

# 업로드
git push

# 원격 저장소 확인
git remote -v

# 커밋 로그 보기
git log --oneline

# 변경사항 비교
git diff
git diff --staged
```

---

## ⚠️ 에러 대응
```bash
# push 안 될 때
git pull origin main
git push

# 서로 다른 히스토리
git pull origin main --allow-unrelated-histories
```

---

## 📁 .gitignore 예시
```gitignore
__pycache__/
*.pyc
.venv/
.env
teacher_practice/
```

---

## 🧠 커밋 메시지 예시
```bash
git commit -m "TIL 정리 및 실습 코드 추가"
git commit -m "RandomForest 모델 비교 실습"
git commit -m "파일 처리 예제 추가"
git commit -m "머신러닝 분류 모델 성능 비교"
git commit -m "프로젝트 구조 정리"
```

---

## 📂 추천 폴더 구조
```bash
project/
├── git_cheatsheet.md
├── python_cheatsheet.py
├── randomforest-comparison/
│   ├── model_compare.py
│   ├── model_compare_2.py
│   └── TIL.md
```

---

## 💡 핵심 한 줄 정리
```bash
git status → git add . → git commit → git push
```