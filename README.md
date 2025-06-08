# 🎧 MP3 Player - PySide6 GUI
**PySide6를 기반으로 한 데스크탑 MP3 플레이어**

## 📐 UI 구조 및 기능 설명
### ✅ `mainLayout`

음악을 다운로드하고, 로컬 저장소에 있는 음악을 리스트로 확인

원하는 곡을 모아 플레이리스트로 구성

- **`sidebarLayout`**: 음악 다운로드 및 플레이리스트 구성
- **`activityLayout`**: 현재 재생 정보 및 재생 컨트롤 영역

## 📁 sidebarLayout

### 🎵 `playlistBox`
- **`addMusicBtn`**: 로컬에 저장된 음악을 불러와 플레이리스트에 추가

### 🔍 `searchBox`
- **`downloadBtn`**: 음악을 다운로드
- **`downloadListBtn`**: 다운로드한 음악 리스트 보기

### 📑 `songInfoLayout`
- **`artistLabel` / `songTitleLabel`**: 선택된 곡의 가수명 및 제목 표시
- **`musicList (QListWidget)`**: 플레이리스트에 추가된 음악 목록. 이 순서대로 음악이 자동 재생됨

## 🎬 activityLayout

현재 재생 중인 음악 정보를 보여주고, 재생/정지/볼륨 등의 제어 기능을 제공

### 🎼 `nowPlayLayout`
- **`nowTitleLabel`**: 현재 재생 중인 곡의 제목
- **`nowArtistLabel`**: 현재 재생 중인 곡의 가수명

### 🎛️ `playerControl`
#### ▶️ `playControlBar`
- **`prevBtn`**: 이전 곡으로 이동
- **`playBtn`**: 재생 / 일시정지 토글
- **`nextBtn`**: 다음 곡으로 이동

#### ⏱️ `playTimeBar`
- **`playTimeSlider`**: 현재 재생 위치를 슬라이더로 표시 및 조절
- **`playTimeView`**: 현재 시간 / 전체 시간 표시 (예: 0:43 / 3:21)