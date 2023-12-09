from setuptools import setup

if __name__ == "__main__":
    setup(
        # CFFI
        zip_safe=False,
        ext_package="_ljm_cffi_bindings",
        cffi_modules=["src/cffi_build.py:ffibuilder"],
    )
