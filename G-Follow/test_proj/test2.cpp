/*
#include "dcmtk/config/osconfig.h"
#include "dcmtk/dcmdata/dctk.h"
#include "dcmtk/dcmimgle/dcmimage.h"
#include "dcmtk/dcmjpeg/djutils.h"
#include "dcmtk/dcmjpeg/djdecode.h"

#pragma comment(lib, "dcmtk.lib")

void CDCMTK_Image_OutputView::OnDraw(CDC* pDC)
{
	CDCMTK_Image_OutputDoc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;
	// TODO: 여기에 원시 데이터에 대한 그리기 코드를 추가합니다.
	LPCTSTR lpstrFile = _T("C://Users//zxwlg//workspace//2022-1//G-Follow//data//sample.dcm");
	USES_CONVERSION;
	char* filename = W2A(lpstrFile);

	DcmFileFormat* ptrDcmFileFormat = new DcmFileFormat();
	OFCondition cond = ptrDcmFileFormat->loadFile(filename);
	if (cond.good())
	{
		//AfxMessageBox(_T("DCM파일 로드성공"));
	}
	else if (cond.bad())
	{
		AfxMessageBox(_T("DCM파일 로드실패"));
		exit(0);
	}
	DJDecoderRegistration::registerCodecs(); // register JPEG codecs
	DcmDataset* dataset = ptrDcmFileFormat->getDataset();

	// decompress data set if compressed
	dataset->chooseRepresentation(EXS_LittleEndianExplicit, NULL);

	E_TransferSyntax xfer = ptrDcmFileFormat->getDataset()->getOriginalXfer();

	DicomImage* ptrDicomImage = new DicomImage(ptrDcmFileFormat, xfer, CIF_AcrNemaCompatibility, 0, 1);

	if (ptrDicomImage != NULL)
	{
		//AfxMessageBox(_T("DicomImage 인스턴스 생성 성공"));
	}
	else
	{
		AfxMessageBox(_T("DicomImage 인스턴스 생성 실패"));
		exit(0);
	}
	if (ptrDicomImage->getStatus() != EIS_Normal) exit(0);
	int width = (int)ptrDicomImage->getWidth();
	int height = (int)ptrDicomImage->getHeight();
	void* data = NULL;

	int nResult = ptrDicomImage->setMinMaxWindow();

	if (ptrDicomImage->createWindowsDIB(data, width * height) && data) // data 는 사용후 반드시 해제해야 함
	{
		BITMAPINFO bi;
		bi.bmiHeader.biSize = sizeof(bi);
		bi.bmiHeader.biWidth = width;
		bi.bmiHeader.biHeight = -height;
		bi.bmiHeader.biPlanes = 1;
		bi.bmiHeader.biBitCount = 24;
		bi.bmiHeader.biCompression = BI_RGB;
		bi.bmiHeader.biSizeImage = 0;

		// hbmp 는 사용후 반드시 해제해야 함
		HBITMAP hbmp = CreateDIBitmap(pDC->GetSafeHdc(), &bi.bmiHeader, CBM_INIT, data, &bi, DIB_RGB_COLORS);

		if (hbmp)
		{
			HDC memDC = CreateCompatibleDC(pDC->GetSafeHdc()); // memDC 는 사용후 반드시 해제해야 함
			SelectObject(memDC, hbmp);
			SetStretchBltMode(memDC, HALFTONE);
			StretchBlt(pDC->GetSafeHdc(), 0, 0, width, height, memDC, 0, 0, width, height, SRCCOPY)
			DeleteDC(memDC);
			DeleteObject(hbmp);
		}
	}

	//delete data
}

*/