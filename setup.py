from setuptools import find_packages, setup

setup(
    name='py-crypto-automation',
    version='1.0.0',
    license="MIT",
    description='Simple crypto automation tools',
    author='Hmohammad2520',
    author_email='Hmohammad2520@gmail.com',
    url='https://github.com/Hmohammad2520/py-crypto-automation',
    install_requires=[
        'requests==2.32.3',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)