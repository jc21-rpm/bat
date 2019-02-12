%global debug_package %{nil}

Name:           bat
Version:        0.10.0
Release:        1%{?dist}
Summary:        A cat clone with syntax highlighting and Git integration.

Group:          Applications/System
License:        GPLv2
URL:            https://github.com/sharkdp/%{name}

BuildRequires:  cmake, libgit2, openssl-devel, libzip-devel

%description
bat supports syntax highlighting for a large number of programming and markup languages.
bat communicates with git to show modifications with respect to the index.
bat can pipe its own output to less if the output is too large for one screen.
Oh.. you can also use it to concatenate files. Whenever bat detects a non-interactive
terminal, it will fall back to printing the plain file contents.


%prep
wget https://github.com/sharkdp/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
cd %{name}-%{version}

%build
cd %{name}-%{version}
cargo build --release


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp %{name}-%{version}/target/release/bat %{buildroot}/usr/bin/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{name}-%{version}/LICENSE* %{name}-%{version}/*.md
/usr/bin/bat


%changelog
* Tue Feb 12 2019 Jamie Curnow <jc@jc21.com> - 0.10.0-1
- v0.10.0

* Mon Nov 12 2018 Jamie Curnow <jc@jc21.com> - 0.9.0-1
- v0.9.0

* Thu Oct 18 2018 Jamie Curnow <jc@jc21.com> - 0.8.0-1
- v0.8.0

* Mon Sep 24 2018 Jamie Curnow <jc@jc21.com> - 0.7.1-1
- v0.7.1

* Thu Sep 13 2018 Jamie Curnow <jc@jc21.com> - 0.7.0-1
- v0.7.0

* Fri Aug 31 2018 Jamie Curnow <jc@jc21.com> - 0.6.0-1
- Initial spec

