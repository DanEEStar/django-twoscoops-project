class {'postgresql':
}

postgresql::role { "{{ project_name }}_vagrant":
    ensure    => present,
    password  => "test",
    require => Class["postgresql"]
}

class {'postgis':
}

postgresql::database { "{{ project_name }}_vagrant":
    ensure => present,
    owner => "{{ project_name }}_vagrant",
    template_name => "template_postgis",
    require => [Exec["create_postgis_template"], Postgresql::Role["{{ project_name }}_vagrant"]]
}

class {'rabbitmq':
}

rabbitmq::vhost { '{{ project_name }}_vagrant_vhost':
  ensure => present,
}

rabbitmq::user { '{{ project_name }}_vagrant':
  ensure   => present,
  password => "test",
  user_tag => management,
}

rabbitmq::permissions { '{{ project_name }}_vagrant@{{ project_name }}_vagrant_vhost':
  user  => '{{ project_name }}_vagrant',
  vhost => '{{ project_name }}_vagrant_vhost',
  conf  => '.*',
  write => '.*',
  read  => '.*',
}

rabbitmq::user { 'guest':
	ensure => absent,
}