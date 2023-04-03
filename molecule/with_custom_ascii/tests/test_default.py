"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_motd_file(host):
    """Validate motd.cfg file."""
    motd_cfg = host.file("/etc/profile.d/motd.cfg")
    assert motd_cfg.exists
    assert motd_cfg.user == "root"
    assert motd_cfg.group == "root"
    assert motd_cfg.mode == 0o644
    assert motd_cfg.contains("print_info()")

def test_motd_file(host):
    """Validate 00-motd-neofetch file."""
    motd_neofetch = host.file("/etc/update-motd.d/00-motd-neofetch")
    assert motd_neofetch.exists
    assert motd_neofetch.user == "root"
    assert motd_neofetch.group == "root"
    assert motd_neofetch.mode == 0o744
    assert motd_neofetch.contains("#! /bin/sh")
    assert motd_neofetch.contains("neofetch --config /etc/profile.d/motd.cfg")