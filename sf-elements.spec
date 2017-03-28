%global sum    Software Factory disk-image-builder elements and scripts

Name:          sf-elements
Version:       2.5
Release:       1%{?dist}
Summary:       %{sum}
License:       ASL 2.0
URL:           https://softwarefactory-project.io
BuildArch:     noarch
Source0:       HEAD.tgz


%description
%{sum}


%prep
%autosetup -n %{name}-%{version}


%install
install -d -m 0755 %{buildroot}/usr/share/sf-elements
cp -r elements/* %{buildroot}/usr/share/sf-elements


%files
/usr/share/sf-elements/


%changelog
* Thu Mar 30 2017 Tristan Cacqueray - 2.5-1
- Initial packaging
