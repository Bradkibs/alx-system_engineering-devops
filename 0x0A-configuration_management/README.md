# Learning about configuration management tools(Puppet to be specific).
## Resources used
* [Intro to configuration management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
* [Puppet resource type: file](https://www.puppet.com/docs/puppet/5.5/types/file.html)
* [Puppet's declarative language: Modeling instead of scripting](https://www.puppet.com/blog)
* [Puppet lint](http://puppet-lint.com/)
* [Puppet emacs mode](http://puppet-lint.com/)

### Install puppet and puppet Lint first on your machine before proceeding
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
$ gem install puppet-lint
```
If the ruby version is deprecated please use the latest ruby version.
```
$ apt-get install -y ruby
```
