# G팔로미
- 인피니트헬스케어
- 주제 : DICOM Viewer : Automatic Windowing Setting
- DICOM 영상을 판독에 적합하도록 화면에 표시하기 위해서 적절한 Windowing Level/Width 초기값을 계산하여 적용할 필요가 있음.

## dicom_gui6.py
- 최종 결과물
- 마우스 드래그로 영역 설정 -> windowing 값 설정
- percent : 드래그 영역의 CDF 양 끝 percent 잘라내서 windowing 값 설정
- 초기화
- 직접 windowing 값 입력해서 바꾸기

## dicom_gui2.py
- GUI로 dicom file 보기
- 마우스 드래그로 window 값 변경 가능 (가로 : width, 세로 : center)

## dicom_hist~
- dicom file 불러와서 읽음
- histogram을 통해 분석

## dicom_roi~
- 마우스로 roi 영역 지정해서 windowing 값 세팅
