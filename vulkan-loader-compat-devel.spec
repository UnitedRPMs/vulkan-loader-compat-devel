%global debug_package %{nil}

Name:           vulkan-loader-compat-devel
Version:        1.2
Release:        1%{?dist}
Summary:        pkgconfig for compatibility

License:        ASL 2.0
URL:            https://github.com/UnitedRPMs/vulkan-loader-compat-devel
Source0:        README      

BuildRequires:  vulkan-loader-devel
Requires:	vulkan-loader-devel

%description
Pkgconfig for compatibility for vulkan-loader and ffmpeg.



%prep
mkdir -p %{name}-%{version}
%setup -T -D -n %{name}-%{version}

%build
# Nothing here


%install
mkdir -p %{buildroot}/%{_datadir}/pkgconfig
cp -f %{_libdir}/pkgconfig/vulkan.pc %{buildroot}/%{_datadir}/pkgconfig/vulkan.pc

# fix vulkan pkgconfig
sed -i 's|vulkan64|vulkan|g' %{buildroot}/%{_datadir}/pkgconfig/vulkan.pc

%files
%{_datadir}/pkgconfig/vulkan.pc


%changelog
* Sun Dec 20 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.2-1
- Initial build, ready for our ffmpeg
