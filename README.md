<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


[comment]: <> ([![Contributors][contributors-shield]][contributors-url])

[comment]: <> ([![Forks][forks-shield]][forks-url])

[comment]: <> ([![Stargazers][stars-shield]][stars-url])

[comment]: <> ([![Issues][issues-shield]][issues-url])

[comment]: <> ([![MIT License][license-shield]][license-url])


<br />
<div align="center">

<h3 align="center">Complete Parser for Solidity with ANTLR4</h3>

  <p align="center">
    <a href="https://github.com/yjkellyjoo/Solidity-complete-parser/issues">Report Bug</a>
    ·
    <a href="https://github.com/yjkellyjoo/Solidity-complete-parser/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

The currently maintained [Solidity parser by the Solidity team](https://github.com/ethereum/solidity/tree/develop/docs/grammar) focuses on parsing the 'latest stable version' of Solidity. The latest stable version of Solidity is v0.8.11 at the moment of writing, but according to my investigations, more than 99% of Ethereum verified smart contracts are compiled with Solidity v0.6.0 and lower. 

I needed a universal parser which would be compatible with all compiler versions (especially v0.6.0 and lower), so this project is all about building a **complete Solidity parser able to parse all compiler versions of Solidity**. 

This work includes:
1. _[`Solidity Language grammar in ANTLR4`](https://github.com/yjkellyjoo/Solidity-complete-parser/blob/main/Solidity.g4) .g4 format._

   The .g4 grammar is an extension of https://github.com/solidity-parser/antlr, where I have revised the grammar to accept code for all Solidity compiler versions up to v0.8.0.

2. _[`visitor`](https://github.com/yjkellyjoo/Solidity-complete-parser/blob/main/MySolidityVisitor.py) and [`listener`](https://github.com/yjkellyjoo/Solidity-complete-parser/blob/main/MySolidityListener.py) implementation in Python3._

   I went through a lot of twists and turns writing these two because there weren't a lot of examples to refer to. I am opening my code hoping it would help people write their own visitor or listener implementations for their grammar written in ANTLR4. 
 
[comment]: <> (I am open to any questions or need of help, let me know through issues or email. )


### Built With

* [ANTLR4](https://www.antlr.org/)

* [Python3](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started
Following instructions are for those who would like to try out the visitor or the listener. 

### Prerequisites
#### Python 3
Python version 3.8.X (I have used 3.8.5) with [antlr4-python3-runtime](https://pypi.org/project/antlr4-python3-runtime/) package installed.
```sh
$ pip install antlr4-python3-runtime
```
#### (Optional) ANTLR4
If you wish to _edit the .g4 and try out your own grammar_, set up ANTLR4 (I have used version 4.9.2).
* For Windows:
    [Following blog](https://levlaz.org/setting-up-antlr4-on-windows/) gives good step-by-step instructions for Windows.

* For Mac:
  1. install ANTLR
  ```sh
  $ cd /usr/local/lib
  $ curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
  ```
  
  2. add CLASSPATH in .bash_profile or an equivalent startup script (.zshrc)
  ```sh
  $ export CLASSPATH=".:/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH"
  ```

  3. create aliases
  ```sh
  $ alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
  $ alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9.2-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
  ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage
### How to try out the visitor or the listener
I have written a sample code using the visitor and the listener in [`run_parser.py`](https://github.com/yjkellyjoo/Solidity-complete-parser/blob/main/run_parser.py).
Detailed explanation is provided through comments in the code. 

Try them out and play with them by adding code lines in the `main` function!

### (Optional) To regenerate lexer and parser
If you have edited the .g4 file, you will have to regenerate its lexer and parser using the below command. 
```shell
$ antlr4 -o /antlr4-generated/ -Dlanguage=Python3 -visitor Solidity.g4
```

For more information on the usage options, refer to [ANTLR Tool Command Line Options](https://github.com/antlr/antlr4/blob/master/doc/tool-options.md)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the Branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->

## License

Distributed under the GNU General Public License v3.0. See [LICENSE](https://github.com/yjkellyjoo/Solidity-complete-parser/blob/main/LICENSE) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

Yejin Kelly Joo - yejinkellyjoo@gmail.com

Project Link: [github repo](https://github.com/yjkellyjoo/Solidity-complete-parser)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/yjkellyjoo/Solidity-complete-parser.svg?style=for-the-badge
[contributors-url]: https://github.com/yjkellyjoo/Solidity-complete-parser/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/yjkellyjoo/Solidity-complete-parser.svg?style=for-the-badge
[forks-url]: https://github.com/yjkellyjoo/Solidity-complete-parser/network/members
[stars-shield]: https://img.shields.io/github/stars/yjkellyjoo/Solidity-complete-parser.svg?style=for-the-badge
[stars-url]: https://github.com/yjkellyjoo/Solidity-complete-parser/stargazers
[issues-shield]: https://img.shields.io/github/issues/yjkellyjoo/Solidity-complete-parser.svg?style=for-the-badge
[issues-url]: https://github.com/yjkellyjoo/Solidity-complete-parser/issues
[license-shield]: https://img.shields.io/github/license/yjkellyjoo/Solidity-complete-parser.svg?style=for-the-badge
[license-url]: https://github.com/yjkellyjoo/Solidity-complete-parser/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/yejinkellyjoo
[product-screenshot]: images/screenshot.png