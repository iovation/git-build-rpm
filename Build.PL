use Module::Build;

my $exec_path = `git --exec-path`;
chomp $exec_path;
my $man_path = `git --man-path`;
chomp $man_path;

my $build = Module::Build->new(
    module_name        => 'git-build-rpm',
    license            => 'perl',
    dist_version_from  => 'bin/git-build-rpm',
    dist_abstract      => 'Build an RPM from a Git repository',
    dist_author        => 'David E. Wheeler <david.wheeler@iovation.com>',
    pm_files           => {},
    configure_requires => { 'Module::Build' => '0.35' },
    build_requires     => { 'Module::Build' => '0.35' },
    install_path       => { script => $exec_path, bin_doc => $man_path },
    requires           => {
        perl                => '5.010',
        Getopt::Long        => 0,
        List::Util          => 0,
        IPC::System::Simple => 1.17,
        File::Temp          => 0,
        Path::Class         => 0,
        File::Path          => 0,
        File::Copy          => 0,
        File::Basename      => 0,
        Pod::Usage          => 0,
    },
);
use Data::Dump; ddx $build->install_path;
$build->create_build_script;
