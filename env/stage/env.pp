class {'postgresql':
}

postgresql::role { "{{ project_name }}_stage":
    ensure    => present,
    password  => "pw_postgresql_{{ project_name }}_f67GFu2kwmreLgNw",
    require => Class["postgresql"]
}

postgresql::database { "{{ project_name }}_stage":
    ensure => present,
    owner => "{{ project_name }}_stage",
    require => Postgresql::Role["{{ project_name }}_stage"]
}

class {'rabbitmq':
}

rabbitmq::vhost { '{{ project_name }}_stage_vhost':
  ensure => present,
}

rabbitmq::user { '{{ project_name }}_stage':
  ensure   => present,
  password => "pw_rabbitmq_{{ project_name }}_cNgrRRkZ9T6eKCLe",
  user_tag => management,
}

rabbitmq::permissions { '{{ project_name }}_stage@{{ project_name }}_stage_vhost':
  user  => '{{ project_name }}_stage',
  vhost => '{{ project_name }}_stage_vhost',
  conf  => '.*',
  write => '.*',
  read  => '.*',
}

rabbitmq::user { 'guest':
	ensure => absent,
}

# clean up django session
cron { django_clearsessions_{{ project_name }}_stage:
  command => "/srv/www/{{ project_name }}/stage/{{ project_name }}-env/bin/python /srv/www/{{ project_name }}/stage/manage.py clearsessions",
  user    => root,
  hour    => 2,
  minute  => 0
}
