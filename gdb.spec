Name: gdb
Version: 8.2
Release: 4

License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and LGPLv3+ and BSD and Public Domain and GFDL
Source: ftp://sourceware.org/pub/gdb/releases/gdb-%{version}.tar.xz
URL: http://gnu.org/software/gdb/

%global gdb_src gdb-%{version}
%global gdb_build build-%{_target_platform}

%undefine _debuginfo_subpackages

Summary: GNU Project debugger

Recommends: gcc-gdb-plugin%{?_isa}
Recommends: dnf-command(debuginfo-install)
Conflicts: gdb-headless < 7.12-29
Requires: gdb-headless%{?_isa} = %{version}-%{release}
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

%global librpmso librpm.so.8

Recommends: default-yama-scope
Recommends: %{librpmso}()(64bit)

Source1: gdb-gstack.man
Source2: gdbinit

# patchs from redhat
Patch002: gdb-vla-intel-fortran-strides.patch
Patch003: gdb-vla-intel-fortran-vla-strings.patch
Patch004: gdb-vla-intel-stringbt-fix.patch
Patch005: gdb-6.3-ppc64syscall-20040622.patch
Patch006: gdb-6.3-ppc64displaysymbol-20041124.patch
Patch007: gdb-6.3-gstack-20050411.patch
Patch008: gdb-6.3-test-pie-20050107.patch
Patch009: gdb-6.3-test-self-20050110.patch
Patch010: gdb-6.3-test-dtorfix-20050121.patch
Patch011: gdb-6.3-test-movedir-20050125.patch
Patch012: gdb-6.3-threaded-watchpoints2-20050225.patch
Patch013: gdb-6.3-inferior-notification-20050721.patch
Patch014: gdb-6.3-inheritancetest-20050726.patch
Patch015: gdb-6.3-readnever-20050907.patch
Patch016: gdb-6.5-bz203661-emit-relocs.patch
Patch017: gdb-6.5-bz185337-resolve-tls-without-debuginfo-v2.patch
Patch018: gdb-6.5-sharedlibrary-path.patch
Patch019: gdb-6.5-BEA-testsuite.patch
Patch020: gdb-6.5-last-address-space-byte-test.patch
Patch021: gdb-6.5-readline-long-line-crash-test.patch
Patch022: gdb-6.5-bz216711-clone-is-outermost.patch
Patch023: gdb-6.5-bz218379-ppc-solib-trampoline-test.patch
Patch024: gdb-6.5-bz218379-solib-trampoline-lookup-lock-fix.patch
Patch025: gdb-6.5-bz109921-DW_AT_decl_file-test.patch
Patch026: gdb-6.3-bz140532-ppc-unwinding-test.patch
Patch027: gdb-6.3-bz202689-exec-from-pthread-test.patch
Patch028: gdb-6.6-bz230000-power6-disassembly-test.patch
Patch029: gdb-6.6-bz229517-gcore-without-terminal.patch
Patch030: gdb-6.6-testsuite-timeouts.patch
Patch031: gdb-6.6-bz237572-ppc-atomic-sequence-test.patch
Patch032: gdb-6.6-scheduler_locking-step-is-default.patch
Patch033: gdb-6.3-attach-see-vdso-test.patch
Patch034: gdb-6.5-bz243845-stale-testing-zombie-test.patch
Patch035: gdb-6.6-buildid-locate.patch
Patch036: gdb-6.6-buildid-locate-solib-missing-ids.patch
Patch037: gdb-6.6-buildid-locate-rpm.patch
Patch038: gdb-6.7-charsign-test.patch
Patch039: gdb-6.7-ppc-clobbered-registers-O2-test.patch
Patch040: gdb-6.7-testsuite-stable-results.patch
Patch041: gdb-6.5-ia64-libunwind-leak-test.patch
Patch042: gdb-6.5-missed-trap-on-step-test.patch
Patch043: gdb-6.5-gcore-buffer-limit-test.patch
Patch044: gdb-6.3-mapping-zero-inode-test.patch
Patch045: gdb-6.3-focus-cmd-prev-test.patch
Patch046: gdb-6.8-bz442765-threaded-exec-test.patch
Patch047: gdb-6.8-sparc64-silence-memcpy-check.patch
Patch048: gdb-6.5-section-num-fixup-test.patch
Patch049: gdb-6.8-bz436037-reg-no-longer-active.patch
Patch050: gdb-6.8-watchpoint-conditionals-test.patch
Patch051: gdb-6.8-bz466901-backtrace-full-prelinked.patch
Patch052: gdb-simultaneous-step-resume-breakpoint-test.patch
Patch053: gdb-core-open-vdso-warning.patch
Patch054: gdb-x86_64-i386-syscall-restart.patch
Patch055: gdb-bz533176-fortran-omp-step.patch
Patch056: gdb-follow-child-stale-parent.patch
Patch057: gdb-ccache-workaround.patch
Patch058: gdb-archer-pie-addons.patch
Patch059: gdb-archer-pie-addons-keep-disabled.patch
Patch060: gdb-lineno-makeup-test.patch
Patch061: gdb-ppc-power7-test.patch
Patch062: gdb-bz541866-rwatch-before-run.patch
Patch063: gdb-moribund-utrace-workaround.patch
Patch064: gdb-archer-next-over-throw-cxx-exec.patch
Patch065: gdb-bz601887-dwarf4-rh-test.patch
Patch066: gdb-6.6-buildid-locate-core-as-arg.patch
Patch067: gdb-6.6-buildid-locate-rpm-librpm-workaround.patch
Patch068: gdb-test-bt-cfi-without-die.patch
Patch069: gdb-bz568248-oom-is-error.patch
Patch070: gdb-bz634108-solib_address.patch
Patch071: gdb-test-pid0-core.patch
Patch072: gdb-test-dw2-aranges.patch
Patch073: gdb-test-expr-cumulative-archer.patch
Patch074: gdb-physname-pr11734-test.patch
Patch075: gdb-physname-pr12273-test.patch
Patch076: gdb-7.2.50-sparc-add-workaround-to-broken-debug-files.patch
Patch077: gdb-test-ivy-bridge.patch
Patch078: gdb-runtest-pie-override.patch
Patch079: gdb-attach-fail-reasons-5of5.patch
Patch080: gdb-glibc-strstr-workaround.patch
Patch081: gdb-rhel5.9-testcase-xlf-var-inside-mod.patch
Patch082: gdb-rhbz-818343-set-solib-absolute-prefix-testcase.patch
Patch083: gdb-rhbz795424-bitpos-20of25.patch
Patch084: gdb-rhbz795424-bitpos-21of25.patch
Patch085: gdb-rhbz795424-bitpos-22of25.patch
Patch086: gdb-rhbz795424-bitpos-23of25.patch
Patch087: gdb-rhbz795424-bitpos-25of25.patch
Patch088: gdb-rhbz795424-bitpos-25of25-test.patch
Patch089: gdb-rhbz795424-bitpos-lazyvalue.patch
Patch090: gdb-rhbz947564-findvar-assertion-frame-failed-testcase.patch
Patch091: gdb-gnat-dwarf-crash-3of3.patch
Patch092: gdb-rhbz1007614-memleak-infpy_read_memory-test.patch
Patch093: gdb-6.6-buildid-locate-misleading-warning-missing-debuginfo-rhbz981154.patch
Patch094: gdb-archer-vla-tests.patch
Patch095: gdb-vla-intel-tests.patch
Patch096: gdb-btrobust.patch
Patch097: gdb-fortran-frame-string.patch
Patch098: gdb-python-gil.patch
Patch099: gdb-rhbz1156192-recursive-dlopen-test.patch
Patch100: gdb-jit-reader-multilib.patch
Patch101: gdb-rhbz1149205-catch-syscall-after-fork-test.patch
Patch102: gdb-rhbz1186476-internal-error-unqualified-name-re-set-test.patch
Patch103: gdb-rhbz1350436-type-printers-error.patch
Patch104: gdb-rhbz1084404-ppc64-s390x-wrong-prologue-skip-O2-g-3of3.patch
Patch105: gdb-bz1219747-attach-kills.patch
Patch106: gdb-fedora-libncursesw.patch
Patch107: gdb-opcodes-clflushopt-test.patch
Patch108: gdb-dts-rhel6-python-compat.patch
Patch109: gdb-6.6-buildid-locate-rpm-scl.patch
Patch110: gdb-readline62-ask-more-rh.patch
Patch111: gdb-6.8-quit-never-aborts.patch
Patch112: gdb-rhbz1261564-aarch64-hw-watchpoint-test.patch
Patch113: gdb-container-rh-pkg.patch
Patch114: gdb-rhbz1325795-framefilters-test.patch
Patch115: gdb-linux_perf-bundle.patch
Patch116: gdb-libexec-add-index.patch
Patch117: gdb-rhbz1398387-tab-crash-test.patch
Patch118: gdb-testsuite-readline63-sigint.patch
Patch119: gdb-archer.patch
Patch120: gdb-vla-intel-fix-print-char-array.patch
Patch121: gdb-rhbz1553104-s390x-arch12-test.patch
Patch122: gdb-rhbz881849-ipv6-1of3.patch
Patch123: gdb-rhbz881849-ipv6-2of3.patch
Patch124: gdb-rhbz881849-ipv6-3of3.patch
Patch125: gdb-rhbz1187581-power8-regs-1of7.patch
Patch126: gdb-rhbz1187581-power8-regs-2of7.patch
Patch127: gdb-rhbz1187581-power8-regs-3of7.patch
Patch128: gdb-rhbz1187581-power8-regs-4of7.patch
Patch129: gdb-rhbz1187581-power8-regs-5of7.patch
Patch130: gdb-rhbz1187581-power8-regs-6of7.patch
Patch131: gdb-rhbz1187581-power8-regs-7of7.patch
Patch132: gdb-rhbz1491128-batch-mode-exit-status-1of2.patch
Patch133: gdb-rhbz1491128-batch-mode-exit-status-2of2.patch
Patch134: gdb-use-pulongest-aarch64-linux-tdep.patch

BuildRequires: rpm-libs
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
EulerOS %{version}-%{release}
_FOO

rm -f libdecnumber/gstdint.h
rm -f bfd/doc/*.info
rm -f bfd/doc/*.info-*
rm -f gdb/doc/*.info
rm -f gdb/doc/*.info-*
mv -f readline/doc readline-doc
rm -rf readline/*
mv -f readline-doc readline/doc
rm -rf zlib texinfo

%build
rm -rf %{buildroot}
test -e %{_libdir}/%{librpmso}

mkdir %{gdb_build}
cd %{gdb_build}

export CFLAGS="$RPM_OPT_FLAGS -DDNF_DEBUGINFO_INSTALL"
export LDFLAGS="%{?__global_ldflags}"
export CXXFLAGS="$CFLAGS"

if grep -w RL_STATE_FEDORA_GDB %{_includedir}/readline/readline.h;then false;fi

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
rm -rf $RPM_BUILD_ROOT/%{_libdir}/lib{bfd*,opcodes*,iberty*}

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
* Wed Sep 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 8.2-4
- Package init
