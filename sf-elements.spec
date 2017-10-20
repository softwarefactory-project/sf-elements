%global sum    Software Factory disk-image-builder elements and scripts

Name:          sf-elements
Version:       2.5
Release:       2%{?dist}
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
# Make sure all element scripts are executable
find %{buildroot}/usr/share/sf-elements -name "*.d" -type d -exec chmod -R +x {} \;


%files
/usr/share/sf-elements/


%changelog
* Fri Oct 20 2017 Fabien Boucher <fboucher@redhat.com> - 2.5-2
- Make sure all element scripts are executable

* Thu Mar 30 2017 Tristan Cacqueray - 2.5-1
- Initial packaging
