%global tl_name lambda-lists
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Lists in TeXs mouth
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/lambda-lists
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lambda-lists.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lambda-lists.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These list-processing macros avoid the reassignments employed in the
macros shown in Appendix D of the TeXbook: all the manipulations take
place in what Knuth is pleased to call "TeX's mouth".

