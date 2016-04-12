Name:           drpm-rpm-macros
Version:        1
Release:        1%{?dist}
Summary:        RPM macros to enable DRPM

License:        Public Domain
URL:            https://github.com/ignatenkobrain/drpm-rpm-macros

BuildArch:      noarch
Provides:       drpm-macros = %{version}-%{release}

%description
%{summary}.

We have on EL7 and below %bcond_with drpm, but we want to enable DRPM.

%prep
%autosetup -c -D -T

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
echo '%_with_drpm 1' > %{buildroot}/%{_rpmconfigdir}/macros.d/macros.drpm

%files
%{_rpmconfigdir}/macros.d/macros.drpm

%changelog
* Tue Apr 12 2016 Igor Gnatenko <ignatenko@redhat.com> - 1-1
- Initial package
