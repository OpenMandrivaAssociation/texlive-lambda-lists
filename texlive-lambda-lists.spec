# revision 31402
# category Package
# catalog-ctan /macros/generic/lambda-lists
# catalog-date 2013-08-09 20:26:41 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-lambda-lists
Version:	20130809
Release:	2
Summary:	Lists in TeX's mouth
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/lambda-lists
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lambda-lists.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lambda-lists.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
