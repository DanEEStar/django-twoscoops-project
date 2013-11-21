class {'postgresql':
}

postgresql::role { "{{ project_name }}_vagrant":
    ensure    => present,
    password  => "test",
    require => Class["postgresql"]
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