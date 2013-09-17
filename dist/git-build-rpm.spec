Name:    		git-build-rpm
Summary:    	Build an RPM from a Git repository
Version:    	1.1
Release:    	1%{?dist}
Group:          Development/Libraries
License:    	Proprietary
Source0:    	%{name}-%{version}.tar.gz
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  git
BuildRequires:  perl >= 1:v5.10.1
BuildRequires:  perl(Module::Build) >= 0.35
BuildRequires:  perl(Test::Pod) >= 1.20
Requires:       git
Requires:       git-archive-all
Requires:       rpm-build
Requires:       perl(Getopt::Long)
Requires:       perl(List::Util)
Requires:       perl(IPC::System::Simple) >= 1.17
Requires:       perl(File::Temp)
Requires:       perl(Path::Class)
Requires:       perl(File::Path)
Requires:       perl(File::Copy)
Requires:       perl(File::Basename)
Requires:       perl(Pod::Usage)
BuildArch:	    noarch

%define gitbin %(git --exec-path)
%define gitman %(%{__perl} -E 'my $m = `git --man-path`; print $m if $m; ($m = shift) =~ s{libexec\.+}{share/man}; print $m' %{gitbin})

%description
Given a spec file, this program archives the Git repository and creates an RPM
for it.
 
%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Build.PL
./Build

%check
./Build test

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
echo "%{gitman}"
echo "%{gitman}/man1/*"

%clean
%{__rm} -rf  %{buildroot}

%files
%defattr(-,root,root,-)
%{gitman}/man1/*
%{gitbin}/*

%changelog
* Tue Sep 17 2013 David E. Wheeler <david.wheeler@iovation.com> 1.1-1
- Now copies all RPMs, not just `noarch` RPMs (Thanks Damon!).

* Tue Sep 10 2013 David E. Wheeler <david.wheeler@iovation.com> 1.0-1
- Now using `git-archive-all` when creating the archive, so that submodules
  will be archived, as well.

* Wed Jun 5 2013 David E. Wheeler <david.wheeler@iovation.com> 0.99-1
- Now using `git-build-rpm` itself to build the RPM, rather than
  Module::Build::Iovation.
- Added documentation for previously-undocumented option --package-name.

* Wed Dec 5 2012 David E. Wheeler <david.wheeler@iovation.com> 0.98-1
- Updated the Git branch so that if there are multiple possible remote
  branches to choose from, "origin/master" and "*/master" are preferred.

* Thu Nov 29 2012 David E. Wheeler <david.wheeler@iovation.com> 0.97-1
- Fixed bug where detected branch name would lead to a failed build. Now using
  the full branch name for archiving the repository, and using the last part
  of the directory name only if we need to generate a dist tag.

* Thu Nov 29 2012 David E. Wheeler <david.wheeler@iovation.com> 0.96-1
- Fixed bug where the search for a branch name did not include remote
  branches.

* Thu Nov 29 2012 David E. Wheeler <david.wheeler@iovation.com> 0.95-1
- Try even harder to find the current branch mame. If HEAD is detached, see if
  some local branch contains it. If not, see if a remote branch contains it.

* Thu Nov 29 2012 David E. Wheeler <david.wheeler@iovation.com> 0.94-1
- Now try harder to set `--branch` to the current branch name, falling back on
  "HEAD" only if the current checkout is detached.

* Fri Oct 19 2012 David E. Wheeler <david.wheeler@iovation.com> 0.93-1
- Default %dist value now includes the name of the git head, rather than
  "git_head".

* Thu Oct 18 2012 David E. Wheeler <david.wheeler@iovation.com> 0.92-2
- Add missing rpm-build dependency.

* Thu Oct 4 2012 David E. Wheeler <david.wheeler@iovation.com> 0.92-1
- Add missing --package-name option.
- Now exclude ":" when detecting the package name from the git URL.

* Wed Sep 26 2012 David E. Wheeler <david.wheeler@iovation.com> 0.91-3
- Removed Perl modules from `requires_rpms` in Build.PL. They should get
  installed anyway.

* Wed Sep 26 2012 David E. Wheeler <david.wheeler@iovation.com> 0.91-2
- Recommend Test::Pod.

* Wed Sep 26 2012 David E. Wheeler <david.wheeler@iovation.com> 0.91-1
- Upgrade to v0.91.g

* Fri Sep 21 2012 David E. Wheeler <david.wheeler@iovation.com> 0.90-1
- initial RPM
