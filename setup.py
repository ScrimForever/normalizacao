import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="normalizacao",
    version="0.0.1",
    author="Thiago Salgado",
    author_email="thiago.salgado.monteiro@gmail.com",
    description="Pacote com normalizações",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ScrimForever/normalizacao",
    project_urls={
        "Bug Tracker": "https://github.com/ScrimForever/normalizacao/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
