%global debug_package %{nil}

Name:           bat
Version:        0.18.1
Release:        1%{?dist}
Summary:        A cat clone with syntax highlighting and Git integration.
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/sharkdp/%{name}
Source:         https://github.com/sharkdp/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake, libgit2, openssl-devel, libzip-devel, clang-devel

%description
bat supports syntax highlighting for a large number of programming and markup languages.
bat communicates with git to show modifications with respect to the index.
bat can pipe its own output to less if the output is too large for one screen.
Oh.. you can also use it to concatenate files. Whenever bat detects a non-interactive
terminal, it will fall back to printing the plain file contents.

%prep
%setup -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/bat %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
/usr/bin/bat

%changelog
* Mon May 17 2021 Jamie Curnow <jc@jc21.com> - 0.18.1-1
- v0.18.1

* Mon Mar 1 2021 Jamie Curnow <jc@jc21.com> - 0.18.0-1
- v0.18.0

* Wed Nov 25 2020 Jamie Curnow <jc@jc21.com> - 0.17.1-1
- v0.17.1

* Tue Nov 24 2020 Jamie Curnow <jc@jc21.com> - 0.17.0-1
- v0.17.0

* Fri Oct 9 2020 Jamie Curnow <jc@jc21.com> - 0.16.0-1
- v0.16.0

* Thu May 28 2020 Jamie Curnow <jc@jc21.com> - 0.15.4-1
- v0.15.4

* Wed May 27 2020 Jamie Curnow <jc@jc21.com> - 0.15.3-1
- v0.15.3

* Tue May 26 2020 Jamie Curnow <jc@jc21.com> - 0.15.2-1
- v0.15.2

* Tue May 12 2020 Jamie Curnow <jc@jc21.com> - 0.15.1-1
- v0.15.1

* Mon Apr 27 2020 Jamie Curnow <jc@jc21.com> - 0.15.0-1
- v0.15.0

* Tue Mar 24 2020 Jamie Curnow <jc@jc21.com> - 0.13.0-1
- v0.13.0

* Thu Sep 5 2019 Jamie Curnow <jc@jc21.com> - 0.12.1-1
- v0.12.1

* Sun Sep 1 2019 Jamie Curnow <jc@jc21.com> - 0.12.0-1
- v0.12.0

* Thu May 16 2019 Jamie Curnow <jc@jc21.com> - 0.11.0-1
- v0.11.0

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

