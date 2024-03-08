Name: gdb
Version: 14.1
Release: 2

License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and LGPLv3+ and BSD and Public Domain and GFDL-1.3
Source: https://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.xz
URL: http://gnu.org/software/gdb/

Source1: gdb-gstack.man
Source2: gdbinit

# patch from Fedora
Patch1: gdb-6.3-rh-testversion-20041202.patch
Patch2: gdb-6.3-gstack-20050411.patch
Patch3: gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch
Patch4: gdb-6.5-BEA-testsuite.patch
Patch5: gdb-6.5-bz218379-ppc-solib-trampoline-test.patch
Patch6: gdb-6.6-bz229517-gcore-without-terminal.patch
Patch7: gdb-6.6-testsuite-timeouts.patch
Patch8: gdb-6.6-bz237572-ppc-atomic-sequence-test.patch
Patch9: gdb-6.3-attach-see-vdso-test.patch
Patch10: gdb-6.5-bz243845-stale-testing-zombie-test.patch
Patch11: gdb-6.6-buildid-locate.patch
Patch12: gdb-6.6-buildid-locate-solib-missing-ids.patch
Patch13: gdb-6.6-buildid-locate-rpm.patch
Patch14: gdb-6.7-ppc-clobbered-registers-O2-test.patch
Patch15: gdb-6.5-gcore-buffer-limit-test.patch
Patch16: gdb-6.3-mapping-zero-inode-test.patch
Patch17: gdb-6.5-section-num-fixup-test.patch
Patch18: gdb-6.8-bz466901-backtrace-full-prelinked.patch
Patch19: gdb-simultaneous-step-resume-breakpoint-test.patch
Patch20: gdb-core-open-vdso-warning.patch
Patch21: gdb-archer-next-over-throw-cxx-exec.patch
Patch22: gdb-6.6-buildid-locate-rpm-librpm-workaround.patch
Patch23: gdb-test-bt-cfi-without-die.patch
Patch24: gdb-bz634108-solib_address.patch
Patch25: gdb-test-dw2-aranges.patch
Patch26: gdb-glibc-strstr-workaround.patch
Patch27: gdb-rhbz-818343-set-solib-absolute-prefix-testcase.patch
Patch28: gdb-rhbz947564-findvar-assertion-frame-failed-testcase.patch
Patch29: gdb-rhbz1007614-memleak-infpy_read_memory-test.patch
Patch30: gdb-6.6-buildid-locate-misleading-warning-missing-debuginfo-rhbz981154.patch
Patch31: gdb-rhbz1156192-recursive-dlopen-test.patch
Patch32: gdb-rhbz1149205-catch-syscall-after-fork-test.patch
Patch33: gdb-rhbz1084404-ppc64-s390x-wrong-prologue-skip-O2-g-3of3.patch
Patch34: gdb-fedora-libncursesw.patch
Patch35: gdb-rhbz1261564-aarch64-hw-watchpoint-test.patch
Patch36: gdb-container-rh-pkg.patch
Patch37: gdb-linux_perf-bundle.patch
Patch38: gdb-add-index.patch
Patch39: gdb-rhbz2232086-refactor-selftest-support.patch
Patch40: gdb-rhbz-2232086-reduce-size-of-gdb-index.patch
Patch41: gdb-rhbz-2232086-cpp-ify-mapped-symtab.patch
Patch42: gdb-rhbz-2232086-generate-gdb-index-consistently.patch
Patch43: gdb-rhbz-2232086-generate-dwarf-5-index-consistently.patch
Patch44: gdb-rhbz2250652-gdbpy_gil.patch
Patch45: gdb-rhbz2250652-avoid-PyOS_ReadlineTState.patch
Patch46: gdb-rhbz2257562-cp-namespace-null-ptr-check.patch
Patch47: gdb-ftbs-swapped-calloc-args.patch
# Fedra patch end

Patch9000: 0001-set-entry-point-when-text-segment-is-missing.patch

%global gdb_src gdb-%{version}
%global gdb_build build-%{_target_platform}
%global __python %{__python3}

%undefine _debuginfo_subpackages

Summary: GNU Project debugger

Recommends: gcc-gdb-plugin
Recommends: dnf-command(debuginfo-install)
Conflicts: gdb-headless < 7.12-29
Requires: gdb-headless = %{version}-%{release}

%description
GDB, the GNU Project debugger, allows you to see what is going on inside
another program while it executes -- or what another program was doing
at the moment it crashed.

This package is only a stub to install gcc-gdb-plugin for 'compile' commands.
See package 'gdb-headless'.

%package headless
Summary: The GNU Project debugger for C, C++, Fortran, Go and other languages

Conflicts: elfutils < 0.149
Provides: bundled(libiberty) = 20180828
Provides: bundled(gnulib) = 20161115
Provides: bundled(binutils) = 20180828
Provides: bundled(md5-gcc) = 20180828

%global librpmso librpm.so.9

Recommends: default-yama-scope
Recommends: %{librpmso}()(64bit)

BuildRequires: rpm-libs autoconf
BuildRequires: readline-devel >= 6.2-4
BuildRequires: gcc-c++ ncurses-devel texinfo gettext flex bison
BuildRequires: expat-devel xz-devel rpm-devel zlib-devel libselinux-devel
BuildRequires: python3-devel texinfo-tex
BuildRequires: perl-podlators libbabeltrace-devel guile-devel mpfr-devel gmp-devel
%ifarch %{ix86} x86_64
BuildRequires: libipt-devel
%endif

%description headless
GDB, the GNU Project debugger, allows you to see what is going on inside
another program while it executes -- or what another program was doing
at the moment it crashed.

%package gdbserver
Summary: A standalone server for GDB (the GNU source-level debugger)

%description gdbserver
GDB, the GNU Project debugger, allows you to see what is going on inside
another program while it executes -- or what another program was doing
at the moment it crashed.

This package provides a program that allows you to run GDB on a different
machine than the one which is running the program being debugged.

%package help
Summary: Documentation for GDB (the GNU Project debugger)
License: GFDL
BuildArch: noarch

%description help
GDB, the GNU Project debugger, allows you to see what is going on inside
another program while it executes -- or what another program was doing
at the moment it crashed.

This package provides INFO, HTML and PDF user manual for GDB.

%prep
%autosetup -n %{gdb_src} -p1

(cd gdb;rm -fv $(perl -pe 's/\\\n/ /' <Makefile.in|sed -n 's/^YYFILES = //p'))

find -name "*.info*"|xargs rm -f

find -name "*.orig" | xargs rm -f

cat > gdb/version.in << _FOO
openEuler %{version}-%{release}
_FOO

rm -f libdecnumber/gstdint.h
rm -f bfd/doc/*.info
rm -f bfd/doc/*.info-*
rm -f gdb/doc/*.info
rm -f gdb/doc/*.info-*
mv -f readline/readline/doc readline-doc
rm -rf readline/readline/*
mv -f readline-doc readline/readline/doc
rm -rf zlib texinfo

%build
rm -rf %{buildroot}
test -e %{_libdir}/%{librpmso}

mkdir %{gdb_build}
cd %{gdb_build}

export CFLAGS="$RPM_OPT_FLAGS -DDNF_DEBUGINFO_INSTALL -fPIC"
export LDFLAGS="%{?__global_ldflags}"
export CXXFLAGS="$CFLAGS"

../configure							\
	--prefix=%{_prefix}					\
	--libdir=%{_libdir}					\
	--sysconfdir=%{_sysconfdir}				\
	--mandir=%{_mandir}					\
	--infodir=%{_infodir}					\
	--with-system-gdbinit=%{_sysconfdir}/gdbinit		\
	--with-gdb-datadir=%{_datadir}/gdb			\
	--enable-gdb-build-warnings=,-Wno-unused		\
	--enable-build-with-cxx					\
	--enable-werror						\
	--with-separate-debug-dir=/usr/lib/debug		\
	--disable-sim						\
	--disable-rpath						\
	--without-stage1-ldflags				\
	--disable-libmcheck					\
	--with-babeltrace					\
	--with-guile						\
	--with-system-readline					\
	--with-expat						\
	--without-libexpat-prefix				\
	--enable-tui						\
	--with-python=%{__python3}				\
	--with-rpm=%{librpmso}			\
	--with-lzma						\
	--without-libunwind					\
	--enable-64-bit-bfd					\
%ifnarch riscv64 loongarch64
	--enable-inprocess-agent				\
%endif
	--with-system-zlib					\
%ifarch %{ix86} x86_64
	--with-intel-pt						\
%else
	--without-intel-pt					\
%endif
	--with-auto-load-dir='$debugdir:$datadir/auto-load'	\
	--with-auto-load-safe-path='$debugdir:$datadir/auto-load'	\
	--enable-targets=aarch64-linux-gnu %{_target_platform}

make %{?_smp_mflags} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" V=1 maybe-configure-gdb
perl -i.relocatable -pe 's/^(D\[".*_RELOCATABLE"\]=" )1(")$/${1}0$2/' gdb/config.status

make %{?_smp_mflags} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" V=1

! grep '_RELOCATABLE.*1' gdb/config.h

cd ..

cd %{gdb_build}
make %{?_smp_mflags} \
     -C gdb/doc {gdb,annotate}{.info,/index.html,.pdf} MAKEHTMLFLAGS=--no-split MAKEINFOFLAGS=--no-split V=1

cp $RPM_BUILD_DIR/%{gdb_src}/gdb/NEWS $RPM_BUILD_DIR/%{gdb_src}

%check

%install
cd %{gdb_build}
rm -rf $RPM_BUILD_ROOT

make %{?_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_prefix}/libexec
mv -f $RPM_BUILD_ROOT%{_bindir}/gdb $RPM_BUILD_ROOT%{_prefix}/libexec/gdb
ln -s -r $RPM_BUILD_ROOT%{_prefix}/libexec/gdb  $RPM_BUILD_ROOT%{_bindir}/gdb

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit.d
touch -r %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit.d
sed 's#%%{_sysconfdir}#%{_sysconfdir}#g' <%{SOURCE2} >$RPM_BUILD_ROOT%{_sysconfdir}/gdbinit
touch -r %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/gdbinit

for i in `find $RPM_BUILD_ROOT%{_datadir}/gdb/python/gdb -name "*.py"`
do
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/version.in $i 
done

%if 0%{?_enable_debug_packages:1}
mkdir -p $RPM_BUILD_ROOT/usr/lib/debug%{_bindir}
cp -p ./gdb/gdb-gdb.py $RPM_BUILD_ROOT/usr/lib/debug%{_bindir}/
for pyo in "" "-O";do
  %{__python3} $pyo -c 'import compileall, re, sys; sys.exit (not compileall.compile_dir("'"$RPM_BUILD_ROOT/usr/lib/debug%{_bindir}"'", 1, "'"/usr/lib/debug%{_bindir}"'"))'
done
%endif # 0%{?_enable_debug_packages:1}

for i in $(echo bin lib $(basename %{_libdir}) sbin|tr ' ' '\n'|sort -u);do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load/%{_prefix}/$i
  ln -s $(echo %{_prefix}|sed 's#^/*##')/$i \
        $RPM_BUILD_ROOT%{_datadir}/gdb/auto-load/$i
done

for i in `find $RPM_BUILD_ROOT%{_datadir}/gdb -name "*.py"`; do
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/version.in $i
done

# Remove part of binutils files
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/
rm -f $RPM_BUILD_ROOT%{_infodir}/bfd*
rm -f $RPM_BUILD_ROOT%{_infodir}/standard*
rm -f $RPM_BUILD_ROOT%{_infodir}/configure*
rm -f $RPM_BUILD_ROOT%{_infodir}/sframe-spec*
rm -rf $RPM_BUILD_ROOT%{_includedir}/*.h
rm -rf $RPM_BUILD_ROOT/%{_libdir}/lib{bfd*,opcodes*,iberty*,ctf*,sframe*}

cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/gstack.1
ln -s gstack.1 $RPM_BUILD_ROOT%{_mandir}/man1/pstack.1
ln -s gstack $RPM_BUILD_ROOT%{_bindir}/pstack

# Packaged GDB is not a cross-target one.
(cd $RPM_BUILD_ROOT%{_datadir}/gdb/syscalls
 rm -f mips*.xml
 rm -f sparc*.xml
%ifnarch x86_64
 rm -f amd64-linux.xml
%endif
%ifnarch %{ix86} x86_64
 rm -f i386-linux.xml
%endif
)

# Remove.
rm -f $RPM_BUILD_ROOT%{_infodir}/gdbint*
rm -f $RPM_BUILD_ROOT%{_infodir}/stabs*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/system-gdbinit/elinos.py
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/system-gdbinit/wrs-linux.py
rmdir $RPM_BUILD_ROOT%{_datadir}/gdb/system-gdbinit
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/python/gdb/FrameWrapper.py
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/python/gdb/backtrace.py
rm -f $RPM_BUILD_ROOT%{_datadir}/gdb/python/gdb/command/backtrace.py

%files
%license COPYING3 COPYING COPYING.LIB COPYING3.LIB
%doc README NEWS
%{_bindir}/gdb
%{_bindir}/gcore
%{_bindir}/gstack
%{_bindir}/pstack
%{_includedir}/gdb

%files headless
%{_prefix}/libexec/gdb
%config(noreplace) %{_sysconfdir}/gdbinit
%{_sysconfdir}/gdbinit.d
%{_bindir}/gdb-add-index
%{_datadir}/gdb

%files gdbserver
%{_bindir}/gdbserver
%ifnarch riscv64 loongarch64
%{_libdir}/libinproctrace.so
%endif

%files help
%{_mandir}/*/gcore.1*
%{_mandir}/*/gstack.1*
%{_mandir}/*/pstack.1*
%{_mandir}/*/gdb.1*
%{_mandir}/*/gdbinit.5*
%{_mandir}/*/gdb-add-index.1*
%{_mandir}/*/gdbserver.1*
%doc %{gdb_build}/gdb/doc/{gdb,annotate}.{html,pdf}
%{_infodir}/annotate.info*
%{_infodir}/gdb.info*
%{_infodir}/ctf-spec.info.gz

%changelog
* Wed Mar  6 2024 Wenlong Zhang <zhangwenlong@loongson.cn> - 14.1-2
- Fix build error for loongarch64

* Wed Jan 24 2024 liuchao <liuchao173@huawei.com> - 14.1-1
- upgrade GDB version to 14.1:
  - GDB no longer support AiX 4.x, 5.x and 6.x. The minimum version supported is AiX 7.1.
  - GDB/MI version 1 support has been removed
  - Initial built-in support for Debugger Adapter Protocol (DAP)
  - GDB now recognizes the NO_COLOR environment variable
  - Initial support for integer types larger than 64 bits
  - Breakpoints can now be inferior-specific
  - New convenience function "$_shell", to execute a shell command and return its result.
  - Python support
  - Support for enabling or disabling individual remote target features
  - New 'no-history' stop reason
  - Support for inferior-specific breakpoints
  - The bkpt tuple, which appears in breakpoint-created notifications, and in the result of the -break-insert command can now include an optional 'inferior' field for both the main breakpoint, and each location, when the breakpoint is inferior-specific.
  - Trying to create a thread-specific breakpoint using a non-existent thread ID now results in an error
  - New "simple-values-ref-types" -list-feature value indicating how the --simple-values option in various commands take reference types into account.
  - Initial support for Scalable Matrix Extension (SME) and for Scalable Matrix Extension 2 (SME2)
  - The 'org.gnu.gdb.aarch64.pauth' Pointer Authentication feature is now deprecated in favor of the 'org.gnu.gdb.aarch64.pauth_v2' feature string
  - Support for the Ada 2022 target name symbol ('@')
  - Support for the The Ada 2022 'Enum_Rep and 'Enum_Val attributes
  - The 'list' command now accepts '.' as an argument, telling GDB to print the location around the point of execution within the current frame
  - New '%V' output format for printf and dprintf commands.
  - The printf command now limits the size of strings fetched from the inferior to the value of the 'max-value-size' setting.
  - Support for extending at configure time the default value of the 'debug-file-directory' GDB parameter via the new --additional-debug-dirs=PATHs configure option.
  - New command "info main"
  - New command "set tui mouse-events [on|off]" (on by default)
  - New command "set always-read-ctf on|off" (off by default)
  - Various new debug and maitenance commands

* Tue Nov 21 2023 Wenyu Liu <liuwenyu7@huawei.com> - 12.1-10
- fix CVE-2023-39130

* Tue Nov 21 2023 Wenyu Liu <liuwenyu7@huawei.com> - 12.1-9
- some follow-up patches of CVE-2023-39129

* Thu Oct 12 2023 liningjie <liningjie@xfusion.com> - 12.1-8
- fix CVE-2023-39129

* Sat Sep 2 2023 liningjie <liningjie@xfusion.com> - 12.1-7
- fix CVE-2023-39128

* Thu Aug 3 2023 Wenyu Liu <liuwenyu7@huawei.com> - 12.1-6
- libctf: update regexp to allow makeinfo to build document

* Thu Jul 27 2023 Wenyu Liu <liuwenyu7@huawei.com> - 12.1-5
- Handle Python 3.11 deprecation of PySys_SetPath and Py_SetProgramName

* Thu Jul 27 2023 Wenyu Liu <liuwenyu7@huawei.com> - 12.1-4
- initialize the data_head variable to eliminate compilation warnings

* Tue Feb 14 2023 Wenyu Liu <liuwenyu7@huawei.com> - 12.1-3
- Rectify the spec file.

* Mon Feb 6 2023 Wenyu Liu <liuwenyu7@huawei.com> - 12.1-2
- Add support for readline 8.2

* Fri Nov 18 2022 yaowenbin <yaowenbin1@huawei.com> - 12.1-1
- upgrade GDB version to 12.1

* Mon Aug 15 2022 laokz <laokz@foxmail.com> - 11.1-4
- fix riscv64 relevant config

* Fri Jul  8 2022 cenhuilin <cenhuilin@kylinos.cn> - 11.1-3
- set entry point when text segment is missing

* Tue Apr 12 2022 zhouwenpei <zhouwenpei1@h-partners.com> - 11.1-2
- fix gdb build error via cherry-pick upstream patch

* Wed Dec 8 2021 zhouwenpei <zhouwenpei1@huawei.com> - 11.1-1
- upgrade GDB version to 11.1

* Fri Aug 13 2021 zhouwenpei <zhouwenpei1@huawei.com> - 9.2-7
- adjust include order to avoid gnulib error

* Fri Jul 23 2021 zhouwenpei <zhouwenpei1@huawei.com> - 9.2-6
- remove unnecessary build require.

* Mon Apr 19 2021 yuxiangyang <yuxiangyang4@huawei.com> - 9.2-5
- remove unnecessary build require.

* Mon Apr 19 2021 yuxiangyang <yuxiangyang4@huawei.com> - 9.2-5
- remove unnecessary build require.

* Wed Mar 31 2021 xinghe <xinghe1@huawei.com> - 9.2-4
- fix typo for name

* Sat Nov 7 2020 Qingqing Li<liqingqing3@huawei.com> - 9.2-3
- cause riscv64 do not support gdbserver, create a empty package for it.
- add -fPIC option.

* Sun Sep 13 2020 licihua<licihua@huawei.com> - 9.2-2
- Change the sequence of patch and sources

* Wed Jul 22 2020 qinyu<qinyu16@huawei.com> - 9.2-1
- upgrade GDB version to 9.2

* Wed Apr  8 2020 Yunfeng Ye<yeyunfeng@huawei.com> - 8.3.1-12
- remove some useless information for cleancode

* Wed Mar 11 2020 yuxiangyang<yuxiangyang4@huawei.com> - 8.3.1-11
- backport upstream patch to fix hang in stop_all_stop

* Mon Feb  3 2020 yuxiangyang<yuxiangyang4@huawei.com> - 8.3.1-10
- fix CVE-2017-9778

* Thu Jan 16 2020 openEuler Buildteam <buildteam@openeuler.org> - 8.3.1-9
- rpm upgrade successful, delete the dependence to librpm8

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 8.3.1-8
- add build requirement librpm8

* Wed Jan  8 2020 openEuler Buildteam <buildteam@openeuler.org> - 8.3.1-7
- Upgrade GDB version to 8.3.1

* Tue Dec 24 2019 yuxiangyang<yuxiangyang4@huawei.com> - 8.2-6
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: Modify the requirement about python2/3 when compilation rpm.

* Thu Dec 19 2019 yeyunfeng<yeyunfeng@huawei.com> - 8.2-5
- Type:cves
- ID:CVE-2017-9778
- SUG:NA
- DESC: fix CVE-2017-9778

* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.2-4
- Package init
