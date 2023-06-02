from setuptools import setup

included_packages = ['oc_dlinterface']

__version = '1.0.0'

spec = {
    'name': 'oc_dlinterface',
    'version': __version,
    'description': 'dl interface',
    'long_description': '',
    'long_description_content_type': 'text/plain',
    'install_requires': [
        'oc_cdt_queue2'],
    'packages': included_packages,
    'python_requires': '>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*'
}

setup (**spec)

