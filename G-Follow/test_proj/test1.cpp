#include "dcmtk/config/osconfig.h"
#include "dcmtk/dcmdata/dctk.h"
#include <iostream>

#pragma comment(lib, "dcmtk.lib")

using namespace std;

int main()
{
    DcmFileFormat fileformat;
    OFCondition status = fileformat.loadFile("C://Users//zxwlg//workspace//2022-1//G-Follow//data//Sample1/4625.38405.33988.17340.36372.43091.37138.15103.100.0.dcm");
    if (status.good())
    {
        OFString patientName;
        if (fileformat.getDataset()->findAndGetOFString(DCM_PatientName, patientName).good())
        {
            cout << "Patient's Name: " << patientName << endl;
        }
        else
        {
            cerr << "Error: cannot access Patient's Name!" << endl;
        }
    }
    else
    {
        cerr << "Error: cannot read DICOM file (" << status.text() << ")" << endl;
    }
    return 0;
}
