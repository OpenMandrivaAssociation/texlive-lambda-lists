Name:		texlive-lambda-lists
Version:	31402
Release:	1
Summary:	Lists in TeX's mouth
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/lambda-lists
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lambda-lists.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lambda-lists.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These list-processing macros avoid the reassignments employed
in the macros shown in Appendix D of the TeXbook: all the
manipulations take place in what Knuth is pleased to call
"TeX's mouth".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/lambda-lists/lambda.sty
%doc %{_texmfdistdir}/doc/plain/lambda-lists/README
%doc %{_texmfdistdir}/doc/plain/lambda-lists/lambda-lists.pdf
%doc %{_texmfdistdir}/doc/plain/lambda-lists/lambda-lists.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
