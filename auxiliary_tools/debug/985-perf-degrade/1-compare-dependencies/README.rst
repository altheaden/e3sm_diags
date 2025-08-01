
Accoding to ``compare_envs.py``, the latest e3sm_unified environment (v1.11.1)
and e3sm_diags_dev_985 environment has the following differences in dependencies.

Key Dependency Version Summary
===============================

+------------+---------------------+------------------+
| Dependency | e3sm_diags_dev_985  | e3sm_unified     |
+============+=====================+==================+
| python     | 3.13.3              | 3.10.16          |
+------------+---------------------+------------------+
| numpy      | 2.2.6               | 2.2.4            |
+------------+---------------------+------------------+
| dask       | 2025.5.1            | 2024.11.2        |
+------------+---------------------+------------------+
| xarray     | 2025.4.0            | 2025.1.1         |
+------------+---------------------+------------------+
| esmf       | 8.8.1               | 8.8.0            |
+------------+---------------------+------------------+
| xesmf      | 0.8.10              | 0.8.8            |
+------------+---------------------+------------------+


Overlapping dependencies with different versions:
aws-c-auth: e3sm_diags_dev_985='0.9.0', e3sm_unified='0.8.7'
aws-c-cal: e3sm_diags_dev_985='0.9.2', e3sm_unified='0.8.7'
aws-c-common: e3sm_diags_dev_985='0.12.3', e3sm_unified='0.12.1'
aws-c-http: e3sm_diags_dev_985='0.10.2', e3sm_unified='0.9.5'
aws-c-io: e3sm_diags_dev_985='0.19.1', e3sm_unified='0.17.0'
aws-c-mqtt: e3sm_diags_dev_985='0.13.1', e3sm_unified='0.12.2'
aws-c-s3: e3sm_diags_dev_985='0.8.1', e3sm_unified='0.7.13'
aws-c-sdkutils: e3sm_diags_dev_985='0.2.4', e3sm_unified='0.2.3'
aws-checksums: e3sm_diags_dev_985='0.2.7', e3sm_unified='0.2.3'
aws-crt-cpp: e3sm_diags_dev_985='0.32.8', e3sm_unified='0.31.1'
beautifulsoup4: e3sm_diags_dev_985='4.13.4', e3sm_unified='4.13.3'
bokeh: e3sm_diags_dev_985='3.7.3', e3sm_unified='3.7.2'
bottleneck: e3sm_diags_dev_985='1.5.0', e3sm_unified='1.4.2'
ca-certificates: e3sm_diags_dev_985='2025.4.26', e3sm_unified='2025.1.31'
certifi: e3sm_diags_dev_985='2025.4.26', e3sm_unified='2025.1.31'
cf_xarray: e3sm_diags_dev_985='0.10.5', e3sm_unified='0.10.4'
charset-normalizer: e3sm_diags_dev_985='3.4.2', e3sm_unified='3.4.1'
click: e3sm_diags_dev_985='8.2.1', e3sm_unified='8.1.8'
contourpy: e3sm_diags_dev_985='1.3.2', e3sm_unified='1.3.1'
dask: e3sm_diags_dev_985='2025.5.1', e3sm_unified='2024.11.2'
dask-core: e3sm_diags_dev_985='2025.5.1', e3sm_unified='2024.11.2'
debugpy: e3sm_diags_dev_985='1.8.14', e3sm_unified='1.8.13'
distributed: e3sm_diags_dev_985='2025.5.1', e3sm_unified='2024.11.2'
esmf: e3sm_diags_dev_985='8.8.1', e3sm_unified='8.8.0'
esmpy: e3sm_diags_dev_985='8.8.1', e3sm_unified='8.8.0'
exceptiongroup: e3sm_diags_dev_985='1.3.0', e3sm_unified='1.2.2'
executing: e3sm_diags_dev_985='2.2.0', e3sm_unified='2.1.0'
fonttools: e3sm_diags_dev_985='4.58.2', e3sm_unified='4.57.0'
fsspec: e3sm_diags_dev_985='2025.5.1', e3sm_unified='2025.3.2'
hdf5: e3sm_diags_dev_985='1.14.6', e3sm_unified='1.14.3'
importlib-metadata: e3sm_diags_dev_985='8.7.0', e3sm_unified='8.6.1'
ipython: e3sm_diags_dev_985='9.3.0', e3sm_unified='8.35.0'
joblib: e3sm_diags_dev_985='1.5.1', e3sm_unified='1.4.2'
jupyter_client: e3sm_diags_dev_985='8.6.3', e3sm_unified='7.4.9'
jupyter_core: e3sm_diags_dev_985='5.8.1', e3sm_unified='5.7.2'
libarrow: e3sm_diags_dev_985='20.0.0', e3sm_unified='19.0.1'
libarrow-acero: e3sm_diags_dev_985='20.0.0', e3sm_unified='19.0.1'
libarrow-dataset: e3sm_diags_dev_985='20.0.0', e3sm_unified='19.0.1'
libarrow-substrait: e3sm_diags_dev_985='20.0.0', e3sm_unified='19.0.1'
libcurl: e3sm_diags_dev_985='8.14.1', e3sm_unified='8.13.0'
libdeflate: e3sm_diags_dev_985='1.24', e3sm_unified='1.23'
libgcc: e3sm_diags_dev_985='15.1.0', e3sm_unified='14.2.0'
libgcc-ng: e3sm_diags_dev_985='15.1.0', e3sm_unified='14.2.0'
libgcrypt-lib: e3sm_diags_dev_985='1.11.1', e3sm_unified='1.11.0'
libgfortran: e3sm_diags_dev_985='15.1.0', e3sm_unified='14.2.0'
libgfortran5: e3sm_diags_dev_985='15.1.0', e3sm_unified='14.2.0'
libgomp: e3sm_diags_dev_985='15.1.0', e3sm_unified='14.2.0'
libgpg-error: e3sm_diags_dev_985='1.55', e3sm_unified='1.51'
libjpeg-turbo: e3sm_diags_dev_985='3.1.0', e3sm_unified='3.0.0'
libopentelemetry-cpp: e3sm_diags_dev_985='1.21.0', e3sm_unified='1.20.0'
libopentelemetry-cpp-headers: e3sm_diags_dev_985='1.21.0', e3sm_unified='1.20.0'
libparquet: e3sm_diags_dev_985='20.0.0', e3sm_unified='19.0.1'
libsqlite: e3sm_diags_dev_985='3.50.1', e3sm_unified='3.49.1'
libstdcxx: e3sm_diags_dev_985='15.1.0', e3sm_unified='14.2.0'
libstdcxx-ng: e3sm_diags_dev_985='15.1.0', e3sm_unified='14.2.0'
libsystemd0: e3sm_diags_dev_985='257.6', e3sm_unified='257.4'
libudev1: e3sm_diags_dev_985='257.6', e3sm_unified='257.4'
libxml2: e3sm_diags_dev_985='2.13.8', e3sm_unified='2.13.7'
lxml: e3sm_diags_dev_985='5.4.0', e3sm_unified='5.3.2'
lz4: e3sm_diags_dev_985='4.4.4', e3sm_unified='4.3.3'
mache: e3sm_diags_dev_985='1.31.0', e3sm_unified='1.28.0'
matplotlib-base: e3sm_diags_dev_985='3.10.3', e3sm_unified='3.9.4'
narwhals: e3sm_diags_dev_985='1.42.0', e3sm_unified='1.34.1'
netcdf-fortran: e3sm_diags_dev_985='4.6.2', e3sm_unified='4.6.1'
nlohmann_json: e3sm_diags_dev_985='3.12.0', e3sm_unified='3.11.3'
numpy: e3sm_diags_dev_985='2.2.6', e3sm_unified='2.2.4'
orc: e3sm_diags_dev_985='2.1.2', e3sm_unified='2.1.1'
packaging: e3sm_diags_dev_985='25.0', e3sm_unified='24.2'
pandas: e3sm_diags_dev_985='2.3.0', e3sm_unified='2.2.3'
pillow: e3sm_diags_dev_985='11.2.1', e3sm_unified='10.4.0'
pip: e3sm_diags_dev_985='25.1.1', e3sm_unified='25.0.1'
platformdirs: e3sm_diags_dev_985='4.3.8', e3sm_unified='4.3.7'
pluggy: e3sm_diags_dev_985='1.6.0', e3sm_unified='1.5.0'
proj: e3sm_diags_dev_985='9.6.2', e3sm_unified='9.5.1'
prompt-toolkit: e3sm_diags_dev_985='3.0.51', e3sm_unified='3.0.50'
pyarrow: e3sm_diags_dev_985='20.0.0', e3sm_unified='19.0.1'
pyarrow-core: e3sm_diags_dev_985='20.0.0', e3sm_unified='19.0.1'
pyproj: e3sm_diags_dev_985='3.7.1', e3sm_unified='3.7.0'
pytest: e3sm_diags_dev_985='8.4.0', e3sm_unified='8.3.5'
python: e3sm_diags_dev_985='3.13.3', e3sm_unified='3.10.16'
python_abi: e3sm_diags_dev_985='3.13', e3sm_unified='3.10'
pytz: e3sm_diags_dev_985='2025.2', e3sm_unified='2024.1'
requests: e3sm_diags_dev_985='2.32.4', e3sm_unified='2.32.3'
s2n: e3sm_diags_dev_985='1.5.21', e3sm_unified='1.5.15'
scikit-learn: e3sm_diags_dev_985='1.7.0', e3sm_unified='1.6.1'
setuptools: e3sm_diags_dev_985='80.9.0', e3sm_unified='78.1.0'
shapely: e3sm_diags_dev_985='2.1.1', e3sm_unified='2.1.0'
soupsieve: e3sm_diags_dev_985='2.7', e3sm_unified='2.5'
sparse: e3sm_diags_dev_985='0.17.0', e3sm_unified='0.16.0'
sqlite: e3sm_diags_dev_985='3.50.1', e3sm_unified='3.49.1'
tornado: e3sm_diags_dev_985='6.5.1', e3sm_unified='6.4.2'
typing-extensions: e3sm_diags_dev_985='4.14.0', e3sm_unified='4.13.2'
typing_extensions: e3sm_diags_dev_985='4.14.0', e3sm_unified='4.13.2'
urllib3: e3sm_diags_dev_985='2.4.0', e3sm_unified='2.3.0'
xarray: e3sm_diags_dev_985='2025.4.0', e3sm_unified='2025.1.1'
xcdat: e3sm_diags_dev_985='0.9.0', e3sm_unified='0.8.0'
xesmf: e3sm_diags_dev_985='0.8.10', e3sm_unified='0.8.8'
xyzservices: e3sm_diags_dev_985='2025.4.0', e3sm_unified='2025.1.0'
zipp: e3sm_diags_dev_985='3.23.0', e3sm_unified='3.21.0'
