
# This manuscript fixes an internal 500 server error and runs command using puppet

$to_be_edited = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${to_be_edited}",
  path    => ['/bin','/usr/bin']
}