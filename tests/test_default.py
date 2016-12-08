from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('group1')


def test_hosts_file(File):
    hosts = File('/etc/hosts')
    assert hosts.user == 'root'
    assert hosts.group == 'root'


def test_nginx_package(Package):
    nginx = Package('nginx')
    assert nginx.is_installed


def test_nginx_service(Service):
    nginx = Service('nginx')
    assert nginx.is_running
    assert nginx.is_enabled


def test_vhosts_file(File):
    vhosts = File('/etc/nginx/sites-available/vhosts.conf')
    assert not vhosts.exists
