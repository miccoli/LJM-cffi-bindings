from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source(
    "_ljm",
    """
#include <LabJackM.h>   // the C header of the library
""",
    libraries=["LabJackM"],
)

ffibuilder.cdef(
    """
// constants from header file
static const double LJM_VERSION;

static const int LJM_STRING_MAX_SIZE;
static const int LJM_STRING_ALLOCATION_SIZE;
static const int LJM_MAX_NAME_SIZE;

// dtypes
static const int LJM_UINT16;  // C type of unsigned short
static const int LJM_UINT32;  // C type of unsigned int
static const int LJM_INT32;   // C type of int
static const int LJM_FLOAT32; // C type of float
static const int LJM_BYTE;    // byte array, zero padded to even length
                              // but no null terminator guaranteed
static const int LJM_STRING;  // same as LJM_BYTE but always null terminated


//connection type
static const int LJM_ctANY;
static const int LJM_ctANY_TCP;

static const int LJM_ctUSB;

static const int LJM_ctTCP;
static const int LJM_ctNETWORK_TCP;
static const int LJM_ctETHERNET;
static const int LJM_ctETHERNET_TCP;
static const int LJM_ctWIFI;
static const int LJM_ctWIFI_TCP;

static const int LJM_ctNETWORK_UDP;
static const int LJM_ctETHERNET_UDP;
static const int LJM_ctWIFI_UDP;

static const int LJM_ctNETWORK_ANY;
static const int LJM_ctETHERNET_ANY;
static const int LJM_ctWIFI_ANY;

// call back function
extern "Python" void StreamReadCallback(void *);

// wrapped LJM API
int LJM_Open(
    int DeviceType,
    int ConnectionType,
    const char * Identifier,
    int * Handle);

int LJM_Close(int Handle);

int LJM_eReadAddress(
    int Handle,
    int Address,
    int Type,
    double * Value);

int LJM_eWriteAddress(
    int Handle,
    int Address,
    int Type,
    double Value);

int LJM_eWriteAddressString(
    int Handle,
    int Address,
    const char * String);

int LJM_eReadAddressString(
    int Handle,
    int Address,
    char * String);

int LJM_eStreamStart(
    int Handle,
    int ScansPerRead,
    int NumAddresses,
    const int * aScanList,
    double * ScanRate);

int LJM_eStreamRead(
    int Handle,
    double * aData,
    int * DeviceScanBacklog,
    int * LJMScanBacklog);

int LJM_eStreamStop(int Handle);

typedef void (*LJM_StreamReadCallback)(void *);
int LJM_SetStreamCallback(
    int Handle,
    LJM_StreamReadCallback Callback,
    void * Arg);

int LJM_StreamBurst(
    int Handle,
    int NumAddresses,
    const int * aScanList,
    double * ScanRate,
    unsigned int NumScans,
    double * aData);

int LJM_NameToAddress(
    const char * Name,
    int * Address,
    int * Type);

int LJM_GetHandleInfo(
    int Handle,
    int * DeviceType,
    int * ConnectionType,
    int * SerialNumber,
    int * IPAddress,
    int * Port,
    int * MaxBytesPerMB);

int LJM_ReadLibraryConfigS(
    const char * Parameter,
    double * Value);

int LJM_ReadLibraryConfigStringS(
    const char * Parameter,
    char * String);

int LJM_WriteLibraryConfigS(
    const char * Parameter,
    double Value);

int LJM_WriteLibraryConfigStringS(
    const char * Parameter,
    const char * String);

int LJM_eReadAddresses(
    int Handle,
    int NumFrames,
    const int * aAddresses,
    const int * aTypes,
    double * aValues,
    int * ErrorAddress);

int LJM_eReadAddressArray(
    int Handle,
    int Address,
    int Type,
    int NumValues,
    double * aValues,
    int * ErrorAddress);

int LJM_eReadAddressByteArray(
    int Handle,
    int Address,
    int NumBytes,
    char * aBytes,
    int * ErrorAddress);
"""
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
