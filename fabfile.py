from fabric.api import local


def distribution_register():
    local('python setup.py register')

def distribution_prepare():
    local('python setup.py sdist')

def distribution_distribute():
    local('python setup.py sdist upload')

def setup(modulename):
    samplename = 'sample'
    local("gsed -i 's/%s/%s/g' setup.py" % (samplename, modulename))
    local("mv %s %s" % (samplename, modulename))
    local("mv bin/%sscript bin/%sscript" % (samplename, modulename))
    local("gsed -i 's/%s/%s/g' bin/%sscript" % (samplename, modulename, modulename))
