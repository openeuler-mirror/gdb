Name: gdb
Version: 9.2
Release: 2

License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and LGPLv3+ and BSD and Public Domain and GFDL-1.3
Source: ftp://sourceware.org/pub/gdb/releases/gdb-%{version}.tar.xz
URL: http://gnu.org/software/gdb/

%global gdb_src gdb-%{version}
%global gdb_build build-%{_target_platform}
%global __python %{__python3}

%undefine _debuginfo_subpackages

Summary: GNU Project debugger

Recommends: gcc-gdb-plugin
Recommends: dnf-command(debuginfo-install)
Conflicts: gdb-headless < 7.12-29
Requires: gdb-headless = %{version}-%{release}
BuildRequires: gdb

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

Source1: gdb-gstack.man
Source2: gdbinit

# patch from Fedora
Patch1:    gdb-vla-intel-fortran-strides.patch
Patch2:    gdb-vla-intel-fortran-vla-strings.patch
Patch3:    gdb-vla-intel-stringbt-fix.patch
Patch4:    gdb-6.3-gstack-20050411.patch
Patch5:    gdb-6.3-test-pie-20050107.patch
Patch6:    gdb-6.3-test-self-20050110.patch
Patch7:    gdb-6.3-test-dtorfix-20050121.patch
Patch8:    gdb-6.3-test-movedir-20050125.patch
Patch9:    gdb-6.3-threaded-watchpoints2-20050225.patch
Patch10:   gdb-6.3-inferior-notification-20050721.patch
Patch11:   gdb-6.3-inheritancetest-20050726.patch
Patch12:   gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch
Patch13:   gdb-6.5-sharedlibrary-path.patch
Patch14:   gdb-6.5-BEA-testsuite.patch
Patch15:   gdb-6.5-last-address-space-byte-test.patch
Patch16:   gdb-6.5-readline-long-line-crash-test.patch
Patch17:   gdb-6.5-bz218379-ppc-solib-trampoline-test.patch
Patch18:   gdb-6.5-bz218379-solib-trampoline-lookup-lock-fix.patch
Patch19:   gdb-6.5-bz109921-DW_AT_decl_file-test.patch
Patch20:   gdb-6.3-bz140532-ppc-unwinding-test.patch
Patch21:   gdb-6.3-bz202689-exec-from-pthread-test.patch
Patch22:   gdb-6.6-bz230000-power6-disassembly-test.patch
Patch23:   gdb-6.6-bz229517-gcore-without-terminal.patch
Patch24:   gdb-6.6-testsuite-timeouts.patch
Patch25:   gdb-6.6-bz237572-ppc-atomic-sequence-test.patch
Patch26:   gdb-6.3-attach-see-vdso-test.patch
Patch27:   gdb-6.5-bz243845-stale-testing-zombie-test.patch
Patch28:   gdb-6.6-buildid-locate.patch
Patch29:   gdb-6.6-buildid-locate-solib-missing-ids.patch
Patch30:   gdb-6.6-buildid-locate-rpm.patch
Patch31:   gdb-6.7-charsign-test.patch
Patch32:   gdb-6.7-ppc-clobbered-registers-O2-test.patch
Patch33:   gdb-6.7-testsuite-stable-results.patch
Patch34:   gdb-6.5-ia64-libunwind-leak-test.patch
Patch35:   gdb-6.5-missed-trap-on-step-test.patch
Patch36:   gdb-6.5-gcore-buffer-limit-test.patch
Patch37:   gdb-6.3-mapping-zero-inode-test.patch
Patch38:   gdb-6.3-focus-cmd-prev-test.patch
Patch39:   gdb-6.8-bz442765-threaded-exec-test.patch
Patch40:   gdb-6.5-section-num-fixup-test.patch
Patch41:   gdb-6.8-bz466901-backtrace-full-prelinked.patch
Patch42:   gdb-simultaneous-step-resume-breakpoint-test.patch
Patch43:   gdb-core-open-vdso-warning.patch
Patch44:   gdb-bz533176-fortran-omp-step.patch
Patch45:   gdb-ccache-workaround.patch
Patch46:   gdb-archer-pie-addons.patch
Patch47:   gdb-archer-pie-addons-keep-disabled.patch
Patch48:   gdb-lineno-makeup-test.patch
Patch49:   gdb-ppc-power7-test.patch
Patch50:   gdb-moribund-utrace-workaround.patch
Patch51:   gdb-archer-next-over-throw-cxx-exec.patch
Patch52:   gdb-bz601887-dwarf4-rh-test.patch
Patch53:   gdb-6.6-buildid-locate-core-as-arg.patch
Patch54:   gdb-6.6-buildid-locate-rpm-librpm-workaround.patch
Patch55:   gdb-test-bt-cfi-without-die.patch
Patch56:   gdb-bz634108-solib_address.patch
Patch57:   gdb-test-pid0-core.patch
Patch58:   gdb-test-dw2-aranges.patch
Patch59:   gdb-test-expr-cumulative-archer.patch
Patch60:   gdb-physname-pr11734-test.patch
Patch61:   gdb-physname-pr12273-test.patch
Patch62:   gdb-test-ivy-bridge.patch
Patch63:   gdb-runtest-pie-override.patch
Patch64:   gdb-attach-fail-reasons-5of5.patch
Patch65:   gdb-glibc-strstr-workaround.patch
Patch66:   gdb-rhel5.9-testcase-xlf-var-inside-mod.patch
Patch67:   gdb-rhbz-818343-set-solib-absolute-prefix-testcase.patch
Patch68:   gdb-rhbz947564-findvar-assertion-frame-failed-testcase.patch
Patch69:   gdb-gnat-dwarf-crash-3of3.patch
Patch70:   gdb-rhbz1007614-memleak-infpy_read_memory-test.patch
Patch71:   gdb-6.6-buildid-locate-misleading-warning-missing-debuginfo-rhbz981154.patch
Patch72:   gdb-archer-vla-tests.patch
Patch73:   gdb-vla-intel-tests.patch
Patch74:   gdb-btrobust.patch
Patch75:   gdb-fortran-frame-string.patch
Patch76:   gdb-rhbz1156192-recursive-dlopen-test.patch
Patch77:   gdb-jit-reader-multilib.patch
Patch78:   gdb-rhbz1149205-catch-syscall-after-fork-test.patch
Patch79:   gdb-rhbz1186476-internal-error-unqualified-name-re-set-test.patch
Patch80:   gdb-rhbz1350436-type-printers-error.patch
Patch81:   gdb-rhbz1084404-ppc64-s390x-wrong-prologue-skip-O2-g-3of3.patch
Patch82:   gdb-bz1219747-attach-kills.patch
Patch83:   gdb-fedora-libncursesw.patch
Patch84:   gdb-opcodes-clflushopt-test.patch
Patch85:   gdb-dts-rhel6-python-compat.patch
Patch86:   gdb-6.6-buildid-locate-rpm-scl.patch
Patch87:   gdb-6.8-quit-never-aborts.patch
Patch88:   gdb-rhbz1261564-aarch64-hw-watchpoint-test.patch
Patch89:   gdb-container-rh-pkg.patch
Patch90:   gdb-rhbz1325795-framefilters-test.patch
Patch91:   gdb-linux_perf-bundle.patch
Patch92:   gdb-libexec-add-index.patch
Patch93:   gdb-rhbz1398387-tab-crash-test.patch
Patch94:   gdb-archer.patch
Patch95:   gdb-vla-intel-fix-print-char-array.patch
Patch96:   gdb-rhbz1553104-s390x-arch12-test.patch
Patch97:   gdb-rhbz1818011-bfd-gcc10-error.patch
Patch98:   gdb-rhbz1822715-fix-python-deprecation.patch
Patch99:   gdb-rhbz1829702-fix-python39.patch
Patch100:  gdb-rhbz1844458-use-fputX_unfiltered.patch
Patch101:  gdb-rhbz1838777-debuginfod.patch
# Fedora patch end

BuildRequires: rpm-libs autoconf
BuildRequires: readline-devel >= 6.2-4
BuildRequires: gcc-c++ ncurses-devel texinfo gettext flex bison
BuildRequires: expat-devel xz-devel rpm-devel zlib-devel libselinux-devel
BuildRequires: python3-devel texinfo-tex
BuildRequires: texlive-collection-latexrecommended
BuildRequires: perl-podlators libbabeltrace-devel guile-devel mpfr-devel
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

for i in \
  gdb/python/lib/gdb/FrameWrapper.py \
  gdb/python/lib/gdb/backtrace.py \
  gdb/python/lib/gdb/command/backtrace.py \
  ;do
  test -e $i
  : >$i
done

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

export CFLAGS="$RPM_OPT_FLAGS -DDNF_DEBUGINFO_INSTALL"
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
	--enable-inprocess-agent				\
	--with-system-zlib					\
%ifarch %{ix86} x86_64
	--with-intel-pt						\
%else
	--without-intel-pt					\
%endif
	--with-mpfr						\
	--with-auto-load-dir='$debugdir:$datadir/auto-load'	\
	--with-auto-load-safe-path='$debugdir:$datadir/auto-load'	\
	--enable-targets=aarch64-linux-gnu %{_target_platform}

make %{?_smp_mflags} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" V=1 maybe-configure-gdb
perl -i.relocatable -pe 's/^(D\[".*_RELOCATABLE"\]=" )1(")$/${1}0$2/' gdb/config.status

make %{?_smp_mflags} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" V=1

! grep '_RELOCATABLE.*1' gdb/config.h
grep '^#define HAVE_LIBSELINUX 1$' gdb/config.h
grep '^#define HAVE_SELINUX_SELINUX_H 1$' gdb/config.h

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
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/ChangeLog $i
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
  touch -r $RPM_BUILD_DIR/%{gdb_src}/gdb/ChangeLog $i
done

# Remove part of binutils files
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/
rm -f $RPM_BUILD_ROOT%{_infodir}/bfd*
rm -f $RPM_BUILD_ROOT%{_infodir}/standard*
rm -f $RPM_BUILD_ROOT%{_infodir}/configure*
rm -rf $RPM_BUILD_ROOT%{_includedir}/*.h
rm -rf $RPM_BUILD_ROOT/%{_libdir}/lib{bfd*,opcodes*,iberty*,ctf*}

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
%{_libdir}/libinproctrace.so

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

%changelog
* Wed Mar 31 2021 xinghe<xinghe1@huawei.com> - 9.2-2
- fix typo for name

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
