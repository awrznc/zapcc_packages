Name:     zapcc
Version:  7.0.0
Release:  1
Summary:  zapcc is a caching C++ compiler based on clang, designed to perform faster compilations.
License:  LLVM Release License
Requires: gcc, gcc-c++

%define INSTALLDIR /usr/local/zapcc

%description
zapcc is a caching C++ compiler based on clang, designed to perform faster compilations.

%install
mkdir -p %{buildroot}%{INSTALLDIR}/{bin,lib/clang/7.0.0/include/cuda_wrappers}

install -p -m 755 %{_topdir}../LICENSE.TXT %{buildroot}%{INSTALLDIR}/
install -p -m 755 %{_topdir}../zapcc/build/lib/clang/7.0.0/include/*.h %{buildroot}%{INSTALLDIR}/lib/clang/7.0.0/include/
install -p -m 755 %{_topdir}../zapcc/build/lib/clang/7.0.0/include/cuda_wrappers/* %{buildroot}%{INSTALLDIR}/lib/clang/7.0.0/include/cuda_wrappers/
install -p -m 755 %{_topdir}../zapcc/build/bin/zapcc %{buildroot}%{INSTALLDIR}/bin/
install -p -m 755 %{_topdir}../zapcc/build/bin/zapcc++ %{buildroot}%{INSTALLDIR}/bin/
install -p -m 755 %{_topdir}../zapcc/build/bin/zapcc-cl %{buildroot}%{INSTALLDIR}/bin/
install -p -m 755 %{_topdir}../zapcc/build/bin/zapccs %{buildroot}%{INSTALLDIR}/bin/
install -p -m 755 %{_topdir}../zapcc/build/bin/zapccs.config %{buildroot}%{INSTALLDIR}/bin/

ldconfig

%files
%attr(0755, root, root) %{INSTALLDIR}/*

%clean
rm -rf %{buildroot}%{INSTALLDIR}
