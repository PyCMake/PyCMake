from skbuild import setup

setup(
    name="hello",
    version="1.2.3",
    description="a minimal example package",
    author='the scikit-build team',
    license="MIT",
    packages=['hello'],
    package_dir={'hello': 'hello'},
)
