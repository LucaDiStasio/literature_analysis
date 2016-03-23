#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt, re, mechanize, urllib, urllib2, cookielib, os, time, csv, codecs
from BeautifulSoup import BeautifulSoup
from datetime import datetime
from random import randint

def scrape_mendeley(url, string, outfilename, startpage):
   # Initialize output file
   day = datetime.now().day
   month = datetime.now().month
   year = datetime.now().year
   if outfilename != "":
      pathHTML = str(year) + "_" + str(month) + "_" + str(day) + "_" + outfilename + ".html"
   else:
      pathHTML = str(year) + "_" + str(month) + "_" + str(day) + "_mendeley_search.html"
   
   # Create url for the query
   query = url + string.replace(" ","+")
   
   with codecs.open(pathHTML,'w','utf-8') as fileHTML:
      fileHTML.write('<!doctype html>\n')
      fileHTML.write('<html dir=\"ltr\" lang=\"en-US\">\n')
      fileHTML.write('	<head>\n')
      fileHTML.write('		<title>Thematic Analysis of Scientific Literature</title>\n')
      fileHTML.write('	    <meta charset="UTF-8">\n')
      fileHTML.write('	    <meta name="keywords" content="scientific literature, thematic analysis, machine learning, data mining">\n')
      fileHTML.write('	    <meta name="description" content="Database of scientific literature for thematic analysis">\n')
      fileHTML.write('	    <meta name="author" content="Luca Di Stasio">\n')
      fileHTML.write('	    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">\n')
      fileHTML.write('	    <meta http-equiv="refresh" content="30">\n')
      fileHTML.write('	    <link rel="stylesheet prefetch" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">\n')
      fileHTML.write('	    <link rel="stylesheet prefetch" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\n')
      fileHTML.write('	    <link rel="stylesheet prefetch" href="//fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic">\n')
      fileHTML.write('		<style>\n')
      fileHTML.write('            @font-face {\n')
      fileHTML.write('            font-family:"Minion";\n')
      fileHTML.write('            src:url("/.s/t/1141/fonts/minion.eot");\n')
      fileHTML.write('            src:url("/.s/t/1141/fonts/minion.eot?#iefix") format("embedded-opentype"),\n')
      fileHTML.write('            url("/.s/t/1141/fonts/minion.woff") format("woff"),\n')
      fileHTML.write('            url("/.s/t/1141/fonts/minion.ttf") format("truetype"),\n')
      fileHTML.write('            url("/.s/t/1141/fonts/minion.svg#webfont") format("svg");\n')
      fileHTML.write('            font-weight:normal;\n')
      fileHTML.write('            font-style:normal;\n')
      fileHTML.write('            }\n')
      fileHTML.write('            \n')
      fileHTML.write('            body {background:#fff;margin:0;padding:0;font-size:13px;font-family:Tahoma,Geneva,sans-serif;color:#000;}\n')
      fileHTML.write('            img,form {border:0;margin:0;}\n')
      fileHTML.write('                a,input {outline:none;}\n')
      fileHTML.write('            a {color:#2B63E8;text-decoration:none;}\n')
      fileHTML.write('            a:hover {text-decoration:underline;}\n')
      fileHTML.write('            h1,h2, h3, h4, h5, h6 {font-weight:normal;margin:5px 0;padding:0;}\n')
      fileHTML.write('            h1 {font-size:26px;}\n')
      fileHTML.write('            h2 {font-size:21px;}\n')
      fileHTML.write('            h3 {font-size:19px;}\n')
      fileHTML.write('            h4 {font-size:17px;}\n')
      fileHTML.write('            h5 {font-size:15px;}\n')
      fileHTML.write('            h6 {font-size:13px;}\n')
      fileHTML.write('            ul {list-style:square;}\n')
      fileHTML.write('            hr {clear:both;border:none;border-bottom:1px solid #ddd;padding:10px 0 0;margin:0 0 10px;}\n')
      fileHTML.write('            .clr {clear:both;}\n')
      fileHTML.write('            iframe, object, embed {max-width: 100%;}\n')
      fileHTML.write('            .wrapper {margin:0 auto;}\n')
      fileHTML.write('            #header {background:#3c3c3c url(http://docmase.ucoz.com/1_pdfsam_DocMASE_template_cropped.png) 0 0 no-repeat;background-size:cover;}\n')
      fileHTML.write('            #header-i {background:url(/.s/t/1141/pattern.png);padding:0 0 40px;}\n')
      fileHTML.write('            #site-logo {padding:40px 0 0;}\n')
      fileHTML.write('            .site-l {display:inline-block;position:relative;overflow:hidden;padding:20px 0;}\n')
      fileHTML.write('            .site-l:before {content:"";width:100%;height:30px;position:absolute;top:8px;left:0;background:#2B63E8;z-index:1;-moz-transform:rotate(1deg);-webkit-transform:rotate(1deg);-o-transform:rotate(1deg);-ms-transform:rotate(1deg);transform:rotate(1deg);}\n')
      fileHTML.write('            .site-l:after {content:"";width:100%;height:30px;position:absolute;bottom:8px;left:0;background:#2B63E8;z-index:1;-moz-transform:rotate(-1deg);-webkit-transform:rotate(-1deg);-o-transform:rotate(-1deg);-ms-transform:rotate(-1deg);transform:rotate(-1deg);}\n')
      fileHTML.write('            .site-n {display:inline-block;background:#2B63E8;padding:0 20px;position:relative;color:#fff;font-family:"Minion";font-size:36px;z-index:10;}\n')
      fileHTML.write('            .site-n a {color:#fff;font-weight:bold}\n')
      fileHTML.write('            #promo {padding:0 40px 80px;}\n')
      fileHTML.write('            .promo-ttl {background:#fff;background: rgba(255,255,255,.9);padding:15px 20px;font-family:"Minion";font-size:48px;font-variant:small-caps;font-weight:bold;color:#000;margin:200px 0 20px;display:inline-block;max-width:95%;}\n')
      fileHTML.write('            .promo-ttl a {color:#000;}\n')
      fileHTML.write('            .promo-txt {display:inline-block;background:#fff;background:rgba(255,255,255,.9);padding:15px 20px;font-size:14px;font-weight:bold;line-height:180%;max-width:45%;}\n')
      fileHTML.write('            #nav-box {background:#2B63E8;}\n')
      fileHTML.write('            #catmenu {float:left;width:85%;}\n')
      fileHTML.write('            #catmenu .nav-head,#catmenu ul li em {display:none;}\n')
      fileHTML.write('            #catmenu ul,#catmenu li {margin:0;padding:0;list-style:none;}\n')
      fileHTML.write('            #catmenu li {display:inline-block;padding:0 20px 0 0;}\n')
      fileHTML.write('            #catmenu li.item-parent {position:relative;}\n')
      fileHTML.write('            #catmenu li a {position:relative;display:inline-block;font-size:14px;color:#01267B;line-height:60px;height:60px;text-transform:uppercase;font-weight:bold;}\n')
      fileHTML.write('            #catmenu li > a:hover,#catmenu li > a.uMenuItemA {text-decoration:none;color:#fff;}\n')
      fileHTML.write('            #catmenu ul ul {display:none;padding:10px 15px;background:#C1E145;border-top:2px solid #90ac23;position:absolute;width:180px;top:60px;left:0;z-index:200;}\n')
      fileHTML.write('            #catmenu li li {float:none;display:block;text-align:left;height:auto;padding:0;background:none;border:none;}\n')
      fileHTML.write('            #catmenu li li a {display:block;float:none;height:auto;background:none;border:none;line-height:normal;padding:7px 0;font-size:11px;color:#90ac23;}\n')
      fileHTML.write('            #catmenu li li > a.uMenuItemA,#catmenu li li > a:hover {height:auto;color:#fff;border:none;line-height:normal;}\n')
      fileHTML.write('            #catmenu li li.item-parent > a:after {content:"\\203a";font-size:14px;font-family:Tahoma,Geneva,sans-serif;display:block;width:5px;position:absolute;height:5px;top:4px;left:auto;right:0;}\n')
      fileHTML.write('            #catmenu ul ul ul {left:195px;top:1px;z-index:220;border-top:none;border-left:2px solid #90ac23;}\n')
      fileHTML.write('            #soc-box {float:right;width:15%;text-align:right;line-height:60px;height:60px;}\n')
      fileHTML.write('            #soc-box a {display:inline-block;width:24px;height:24px;line-height:24px;background:url(/.s/t/1141/soc.png);margin:0 0 0 10px;vertical-align:middle;}\n')
      fileHTML.write('            #soc-box a.soc-fc {background-position:0 0;}\n')
      fileHTML.write('            #soc-box a.soc-fc:hover {background-position:-24px 0;}\n')
      fileHTML.write('            #soc-box a.soc-tw {background-position:0 -24px;}\n')
      fileHTML.write('            #soc-box a.soc-tw:hover {background-position:-24px -24px;}\n')
      fileHTML.write('            #soc-box a.soc-vi {background-position:0 -48px;}\n')
      fileHTML.write('            #soc-box a.soc-vi:hover {background-position:-24px -48px;}\n')
      fileHTML.write('            #casing {padding:40px 0;background:#fff;}\n')
      fileHTML.write('            #content {float:left;width:70%;}\n')
      fileHTML.write('            #content.wide-page {float:none;width:auto;}\n')
      fileHTML.write('            #content fieldset {border:2px solid #e6e6e6;padding:20px;margin:10px 0;}\n')
      fileHTML.write('            #content .calTable {margin:0 0 20px;}\n')
      fileHTML.write('            #content .calTable td {padding:12px;}\n')
      fileHTML.write('            .eBlock {margin:0 0 40px;padding:0;border-spacing:0;position:relative;table-layout: fixed;}\n')
      fileHTML.write('            .eBlock + br {display:none;}\n')
      fileHTML.write('            .eBlock + table {margin:0;padding:0;border-spacing:0;position:relative;}\n')
      fileHTML.write('            .eBlock + table td[width="60%"] {font-size:24px;padding:0 0 20px;color:#000;font-family:"Minion";}\n')
      fileHTML.write('            .eBlock td {padding:0!important;}\n')
      fileHTML.write('            .eTitle,.eBlock .eTitle,.eBlock td.eTitle {padding:0!important;font-size:32px;color:#000;font-family:"Minion";}\n')
      fileHTML.write('            .eTitle a {color:#000;}\n')
      fileHTML.write('            .eTitle a:hover {color:#000;text-decoration:none;}\n')
      fileHTML.write('            .eTitle div {padding:0 0 0 10px;}\n')
      fileHTML.write('            .eDetails,.eDetails1,.eDetails2,.eBlock td.eDetails,.eBlock td.eDetails1,.eBlock td.eDetails2 {display:block!important;clear:both;font-size:12px;padding:10px 20px!important;margin:0 0 20px!important;background:#e6e6e6;position:relative;}\n')
      fileHTML.write('            .entryBlock .eDetails {margin-top: 10px!important;}\n')
      fileHTML.write('            .eBlock td.eDetails2, .eBlock td.eDetails1 {display: table-cell!important;}\n')
      fileHTML.write('            .eBlock td.eDetails2 {border-top: 20px solid #fff;}\n')
      fileHTML.write('            .eDetails *,.eDetails1 *,.eDetails2 * {position:relative;z-index:10;}\n')
      fileHTML.write('            .eDetails:before,.eDetails1:before {content:"";width:100%;height:30px;position:absolute;top:-8px;left:0;background:#e6e6e6;z-index:1;-moz-transform:rotate(1deg);-webkit-transform:rotate(1deg);-o-transform:rotate(1deg);-ms-transform:rotate(1deg);transform:rotate(1deg);}\n')
      fileHTML.write('            .eDetails:after,.eDetails1:after {content:"";width:100%;height:30px;position:absolute;bottom:-8px;left:0;background:#e6e6e6;z-index:1;-moz-transform:rotate(-1deg);-webkit-transform:rotate(-1deg);-o-transform:rotate(-1deg);-ms-transform:rotate(-1deg);transform:rotate(-1deg);}\n')
      fileHTML.write('            .eDetails2:after {content:"";width:100%;height:30px;position:absolute;bottom:-8px;left:0;background:#e6e6e6;z-index:1;-moz-transform:rotate(1deg);-webkit-transform:rotate(1deg);-o-transform:rotate(1deg);-ms-transform:rotate(1deg);transform:rotate(1deg);}\n')
      fileHTML.write('            .eDetails2:before {content:"";width:100%;height:30px;position:absolute;top:-8px;left:0;background:#e6e6e6;z-index:1;-moz-transform:rotate(-1deg);-webkit-transform:rotate(-1deg);-o-transform:rotate(-1deg);-ms-transform:rotate(-1deg);transform:rotate(-1deg);}\n')
      fileHTML.write('            .eDetails a,.eDetails1 a,.eDetails2 a {color:#000;text-decoration:underline;}\n')
      fileHTML.write('            .eDetails a:hover,.eDetails1 a:hover,.eDetails2 a:hover {color:#000;text-decoration:none;}\n')
      fileHTML.write('            .eTitle + .eDetails {margin-top: 30px!important;}\n')
      fileHTML.write('            .e-category,.e-comments {background:url(/.s/t/1141/details.png) 0 -500px no-repeat;padding:0 0 0 20px;margin:0 10px 0 0;display:inline-block;line-height:15px;}\n')
      fileHTML.write('            .e-category:hover,.e-comments:hover {background-position:-1000px -500px;}\n')
      fileHTML.write('            .e-reads,.e-loads,.e-author,.e-date,.e-rating,.e-add,.e-tags {background:url(/.s/t/1141/details.png) 0 0 no-repeat;padding:0 0 0 20px;margin:0 10px 0 0;display:inline-block;height:15px;line-height:15px;}\n')
      fileHTML.write('            .e-reads {background-position:0 0;}\n')
      fileHTML.write('           .e-reads:hover {background-position:-1000px 0;}\n')
      fileHTML.write('            .e-loads {background-position:0 -400px;padding:0 0 0 14px;}\n')
      fileHTML.write('            .e-loads:hover {background-position:-1000px -400px;}\n')
      fileHTML.write('            .e-author {background-position:0 -100px;padding:0 0 0 16px;}\n')
      fileHTML.write('            .e-author:hover {background-position:-1000px -100px;}\n')
      fileHTML.write('            .e-date {background-position:0 -300px;padding:0 0 0 20px;}\n')
      fileHTML.write('            .e-date:hover {background-position:-1000px -300px;}\n')
      fileHTML.write('            .e-comments {background-position:0 -200px;}\n')
      fileHTML.write('            .e-comments:hover {background-position:-1000px -200px;}\n')
      fileHTML.write('            .e-rating {background-position:0 -600px;padding:0 0 0 20px;}\n')
      fileHTML.write('            .e-rating:hover {background-position:-1000px -600px;}\n')
      fileHTML.write('            .e-add {background-position:0 -700px;padding:0 0 0 20px;}\n')
      fileHTML.write('            .e-add:hover {background-position:-1000px -700px;}\n')
      fileHTML.write('            .e-tags {background-position:0 -800px;padding:0 0 0 20px;}\n')
      fileHTML.write('            .e-tags:hover {background-position:-1000px -800px;}\n')
      fileHTML.write('            .ed-sep,.ed-title {display:none;}\n')
      fileHTML.write('            .eBlock td.eMessage,.eBlock td.eText,.eMessage,.eText {display:block!important;margin:0!important;padding:20px 0 40px!important;line-height:150%;overflow: hidden;}\n')
      fileHTML.write('            .eMessage img,.eText img {display:block;float:left;border:1px solid #e6e6e6!important;padding:2px!important;margin:5px 20px 15px 0!important; max-width: 100%;}\n')
      fileHTML.write('            .eMessage p,.eText p {margin:0;padding:0 0 5px 0;}\n')
      fileHTML.write('            .eMessage,.eText,.cMessage {word-wrap: break-word;}\n')
      fileHTML.write('            .entryReadAll {display:none;}\n')
      fileHTML.write('            .catPages1,.pagesBlockuz2 {display:block;padding:10px 0 0;}\n')
      fileHTML.write('            .pagesBlockuz1 b,.pagesBlockuz2 b,#pagesBlock1 b,#pagesBlock2 b,.pgSwchA b {display:inline-block;min-width:7px;padding:5px 8px;font-weight:normal;color:#fff;background:#b2d237;font-size:12px;}\n')
      fileHTML.write('            .pagesBlockuz1 a,.pagesBlockuz2 a,#pagesBlock1 a,#pagesBlock2 a,a.pgSwch {display:inline-block;min-width:7px;padding:5px 2px;text-decoration:none;font-size:12px;color:#000;text-decoration:underline;}\n')
      fileHTML.write('            .pagesBlockuz1 a:hover,.pagesBlockuz2 a:hover,#pagesBlock1 a:hover,#pagesBlock2 a:hover,a.pgSwch:hover {color:#000;text-decoration:none;}\n')
      fileHTML.write('            .cBlock1,.cBlock2 {background:#fff;padding:5px!important;margin:0!important;border-bottom:1px solid #e6e6e6;}\n')
      fileHTML.write('            #content .cBlock1,#content .cBlock2{padding:0 0 20px!important;background:none;border-bottom:1px solid #e6e6e6;margin:15px 0 0!important;color:#000;}\n')
      fileHTML.write('            .commTable {margin:40px 0 0;padding:20px;border-spacing:0;border:2px solid #e6e6e6;position:relative;}\n')
      fileHTML.write('            .cMessage {font-size:13px;line-height:130%;}\n')
      fileHTML.write('            .cTop {padding:0 0 15px 0;font-size:12px;color:#8aae01;}\n')
      fileHTML.write('            .cTop * {font-weight:normal;}\n')
      fileHTML.write('            .cAnswer {padding:0 0 0 20px;margin:10px 0 0 45px;border-left:3px solid #8aae01;font-size:13px;color:#8aae01;}\n')
      fileHTML.write('            .commTd1 {padding:5px 2px;width:140px;}\n')
      fileHTML.write('            input.commFl {width:90%;}\n')
      fileHTML.write('            textarea.commFl {width:90%;}\n')
      fileHTML.write('            input.codeButtons {min-width:30px;width:auto!important;padding-left:3px!important;padding-right:3px!important;}\n')
      fileHTML.write('            .securityCode {}\n')
      fileHTML.write('            .eAttach {margin:10px 0; font-size:11px;color:#666;padding:0 0 0 15px;background:url(/.s/t/1141/attach.gif) 0 0 no-repeat;}\n')
      fileHTML.write('            .eRating {font-size:8pt;}\n')
      fileHTML.write('            .manTdError,.commError {color:#f00;}\n')
      fileHTML.write('            .commReg {padding:10px 0;text-align:center;}\n')
      fileHTML.write('            a.groupModer:link,a.groupModer:visited,a.groupModer:hover {color:blue;}\n')
      fileHTML.write('            a.groupAdmin:link,a.groupAdmin:visited,a.groupAdmin:hover {color:red;}\n')
      fileHTML.write('            a.groupVerify:link,a.groupVerify:visited,a.groupVerify:hover {color:green;}\n')
      fileHTML.write('            .replaceTable {font-size:12px;padding:20px;border:2px solid #e6e6e6;background:#fff;}\n')
      fileHTML.write('            .legendTd {font-size:8pt;}\n')
      fileHTML.write('            .outputPM {border:1px dashed #ddd;margin:4px 0 4px 30px;}\n')
      fileHTML.write('            .inputPM {border:1px dashed #447e18;margin:4px 0;}\n')
      fileHTML.write('            .uTable {background:none;border:none;border-spacing:0;}\n')
      fileHTML.write('            .uTable td {padding:10px 20px;border-bottom:1px solid #e6e6e6;}\n')
      fileHTML.write('            .uTable td.uTopTd {font-size:14px;padding-top:0;font-weight:normal!important;}\n')
      fileHTML.write('            .eAttach .entryAttachSize {padding-left:4px;}\n')
      fileHTML.write('            .manTable,#uNetRegF {text-align:left;}\n')
      fileHTML.write('            .manTable .manTd1 {font-size:12px;line-height:14px;width:200px;}\n')
      fileHTML.write('            #casing.popuptable {margin:0;padding:0;background:#fff;color:#000;}\n')
      fileHTML.write('            .popuptitle {font-size:20px;padding:15px 20px;color:#fff;background:#b2d237;text-transform:uppercase;font-weight:bold;text-align:center;}\n')
      fileHTML.write('            .popupbody {padding:20px;font-size:12px;color:#000;padding:20px;}\n')
      fileHTML.write('            .popupbody * {font-size:12px!important;}\n')
      fileHTML.write('            .popuptable table {text-align:left;color:#000;}\n')
      fileHTML.write('            \n')
      fileHTML.write('            .archiveEntryTitle ul {margin:2px 0;list-style:circle;}\n')
      fileHTML.write('            .archiveEntryTitle .archiveEntryTime {display:inline-block;padding:3px 5px;font-size:11px;color:#fff;background:#8aae01;}\n')
      fileHTML.write('            .archiveEntryTitle .archiveEntryTitleLink {font-size:14px;text-decoration:none;}\n')
      fileHTML.write('            .archiveEntryTitle .archiveEntryTitleLink:hover {text-decoration:underline;}\n')
      fileHTML.write('            .archiveEntryTitle .archiveEntryComms {font-size:11px;color:#000;}\n')
      fileHTML.write('            \n')
      fileHTML.write('            .user_avatar img {width:100px;border:1px solid #e6e6e6!important;padding:2px!important;}\n')
      fileHTML.write('            .cMessage .user_avatar img {width:50px;margin:0 10px 5px 0;}\n')
      fileHTML.write('            \n')
      fileHTML.write('            #sidebar {float:right;width:25%;}\n')
      fileHTML.write('            .big-box {margin:0 0 40px;overflow:hidden;}\n')
      fileHTML.write('            .big-ttl {color:#000;font-size:26px;font-family:"Minion";text-align:center;}\n')
      fileHTML.write('            .big-img {padding:0 3px;position:relative;background:#2B63E8;margin:25px 0;}\n')
      fileHTML.write('            .big-img:before {content:"";width:105%;height:45px;position:absolute;top:-13px;left:-5px;background:#2B63E8;z-index:1;-moz-transform:rotate(4deg);-webkit-transform:rotate(4deg);-o-transform:rotate(4deg);-ms-transform:rotate(4deg);transform:rotate(4deg);}\n')
      fileHTML.write('            .big-img:after {content:"";width:105%;height:45px;position:absolute;bottom:-13px;left:-5px;background:#2B63E8;z-index:1;-moz-transform:rotate(-4deg);-webkit-transform:rotate(-4deg);-o-transform:rotate(-4deg);-ms-transform:rotate(-4deg);transform:rotate(-4deg);}\n')
      fileHTML.write('            .big-img img {display:block;width:100%;position:relative;z-index:10;}\n')
      fileHTML.write('            .big-box .inner {font-size:15px;text-align:center;padding:10px 0;}\n')
      fileHTML.write('            \n')
      fileHTML.write('            .sidebox {margin:0 0 20px;padding:0;}\n')
      fileHTML.write('            .sidetitle {font-size:14px;padding:15px 20px;color:#fff;background:#2B63E8;text-transform:uppercase;font-weight:bold;}\n')
      fileHTML.write('            .sidebox .inner {padding:20px;border:2px solid #e6e6e6;border-top:0;}\n')
      fileHTML.write('            .sidebox ul,.sidebox .catsTable {margin:0;padding:0;list-style:none;}\n')
      fileHTML.write('            .sidebox .catsTable,.sidebox .catsTable * {display:block;width:auto!important;}\n')
      fileHTML.write('            .sidebox li,.sidebox .catsTable td {list-style:none;padding:0;}\n')
      fileHTML.write('            .sidebox li a,.sidebox .catsTable td a {display:block;color:#000;padding:5px 0;text-decoration:none;position:relative;font-size:14px;}\n')
      fileHTML.write('             .sidebox li a:before,.sidebox .catsTable td a:before {content:"\\002B";color:#b2b2b2;font-size:16px;font-family:Tahoma,Geneva,sans-serif;padding:0 5px 0 0;}\n')
      fileHTML.write('             .sidebox li a:hover,.sidebox li a.uMenuItemA,.sidebox .catsTable td a:hover,.sidebox .catsTable td a.catNameActive {color:#000;}\n')
      fileHTML.write('             .sidebox li a:hover:after,.sidebox li a.uMenuItemA:after,.sidebox .catsTable td a:hover:after,.sidebox .catsTable td a.catNameActive:after {content:"\\2022";font-size:12px;font-family:Tahoma,Geneva,sans-serif;padding:0 0 0 8px;color:#8aae01;}\n')
      fileHTML.write('             .sidebox li.item-parent {position:relative;}\n')
      fileHTML.write('             .sidebox li.item-parent > a {padding-right:36px;}\n')
      fileHTML.write('             .sidebox li.item-parent em {position:absolute;top:4px;right:0;width:24px;height:24px;line-height:24px;font-style:normal;font-size:14px;text-align:center;z-index:10;cursor:pointer;}\n')
      fileHTML.write('             .sidebox li.item-parent em:hover {color:#8aae01;}\n')
      fileHTML.write('             .sidebox .catNumData {display:none!important;}\n')
      fileHTML.write('             .sidebox .calTable{width:100%;position:relative;}\n')
      fileHTML.write('             .calTable {font-size:12px;}\n')
      fileHTML.write('             .calTable td {text-align:center;padding:6px 2px;}\n')
      fileHTML.write('             .calTable td.calMonth {padding:12px!important;font-size:11px;}\n')
      fileHTML.write('             .calWday,.calWdaySe,.calWdaySu {font-size:11px;color:#000;text-transform:uppercase;}\n')
      fileHTML.write('             .calWdaySe,.calWdaySu {color:#2B63E8;}\n')
      fileHTML.write('             .calTable .calMday {color:#b2b2b2;}\n')
      fileHTML.write('             .calTable .calMdayIs {font-weight:bold;}\n')
      fileHTML.write('             .calTable .calMdayA,.calTable .calMdayIsA {color:#fff;background:#2B63E8;}\n')
      fileHTML.write('             .calTable .calMdayIsA a {color:#fff;}\n')
      fileHTML.write('             .sidebox td.calMonth {position:relative;height:40px;padding:0!important;}\n')
      fileHTML.write('             .sidebox td.calMonth a {position:absolute;}\n')
      fileHTML.write('             .sidebox td.calMonth a:hover {color:#000;text-decoration:none;}\n')
      fileHTML.write('             .sidebox td.calMonth a:first-child,.sidebox td.calMonth > a:first-child + a + a {display:block;text-align:center;width:15px;height:20px;line-height:20px;top:9px;right:10px;font-size:15px;}\n')
      fileHTML.write('             .sidebox td.calMonth a:first-child {right:30px;}\n')
      fileHTML.write('             .sidebox td.calMonth a:first-child + a {font-size:14px;left:10px;top:0;display:inline-block;height:40px;line-height:40px;}\n')
      fileHTML.write('             .sidebox ul ul {display:none;margin:0 0 0 20px;width:auto;padding:0;}\n')
      fileHTML.write('             .sidebox iframe {border:1px solid #e6e6e6;}\n')
      fileHTML.write('             .sidebox .answer {padding:5px 0 0 0;}\n')
      fileHTML.write('             .sidebox input.mchat {max-width:94%;}\n')
      fileHTML.write('             .sidebox textarea.mchat {max-width:90%;}\n')
      fileHTML.write('             .sidebox .loginField {max-width:94%;}\n')
      fileHTML.write('             .schQuery,.schBtn {display:inline;padding:0 2px;}\n')
      fileHTML.write('             .sidebox ul.rate-list {margin:0;}\n')
      fileHTML.write('             #shop-basket ul li a {padding:0;margin:0;border:none;}\n')
      fileHTML.write('             #shop-basket ul li a:before {display:none;}\n')
      fileHTML.write('             .pollButton {padding:10px 0 0;}\n')
      fileHTML.write('             .sidebox .searchForm {background:#fff;border:2px solid #e6e6e6;height:30px;padding:0 34px 0 10px;position:relative;}\n')
      fileHTML.write('             .sidebox .searchForm * {padding:0;margin:0;line-height:normal;}\n')
      fileHTML.write('            .sidebox .schQuery input {background:none!important;border:none!important;width:98%!important;padding:0!important;margin:0!important;height:30px!important;line-height:30px!important;font-size:12px;color:#000;}\n')
      fileHTML.write('             .sidebox .schBtn input {position:absolute;top:0;right:0;border:none!important;padding:0!important;margin:0!important;text-align:left;height:30px!important;width:34px!important;overflow:hidden;text-indent:-10000px;cursor:pointer;background:#2B63E8 url(/.s/t/1141/sch.png) 50% 50% no-repeat!important;}\n')
      fileHTML.write('             .sidebox .schBtn input:hover {background:#6793FB url(/.s/t/1141/sch.png) 50% 50% no-repeat!important;}\n')
      fileHTML.write('             #cont-shop-price .gTableSubTop,#cont-shop-price .forumIcoTd {font-size:13px!important;}\n')
      fileHTML.write('             .shop-info {clear: both;}\n')
      fileHTML.write('             #footer {border-top:1px solid #ddd;padding:35px 0 35px 75px;background:url(/.s/t/1141/footer.png) 0 18px no-repeat;}\n')
      fileHTML.write('             \n')
      fileHTML.write('             .forum-box {clear:both;}\n')
      fileHTML.write('             .gTable {margin:0 0 30px;}\n')
      fileHTML.write('             .gTable,.postTable {background:none;}\n')
      fileHTML.write('             .gTableTop {font-size:32px;color:#000;font-family:"Minion";}\n')
      fileHTML.write('             .gTableTop a {color:#000!important;}\n')
      fileHTML.write('             .gTableTop a:hover {color:#8aae01!important;text-decoration:none!important;}\n')
      fileHTML.write('             .gTableSubTop,.postTdTop {padding:10px 20px;font-size:12px;background:#e6e6e6;}\n')
      fileHTML.write('             .gTableSubTop b {font-weight:normal;}\n')
      fileHTML.write('             .gTableBody,.gTableBody1,.gTableBottom,.gTableError,.forumNameTd,.forumLastPostTd,.threadNametd,.threadAuthTd,.threadLastPostTd,.threadsType,.postPoll,.newThreadBlock,.newPollBlock,.newThreadBlock,.newPollBlock,.gTableRight,.postTdInfo,.codeMessage,.quoteMessage,.forumIcoTd,.forumThreadTd,.forumPostTd,.gTableLeft,.threadIcoTd,.threadPostTd,.threadViewTd,.postBottom,.posttdMessage {padding:10px 20px;border-bottom:1px solid #ddd;}\n')
      fileHTML.write('             .postBottom {padding:3px 0;}\n')
      fileHTML.write('             .posttdMessage {padding:10px 0 12px;}\n')
      fileHTML.write('             a.forum,a.threadLink,a.threadPinnedLink {margin:0 0 5px;display:inline-block;font-size:15px;}\n')
      fileHTML.write('             a.forumLastPostLink {color:#888!important;}\n')
      fileHTML.write('             .gTableLeft {font-weight:bold}\n')
      fileHTML.write('             .gTableError {color:#FF0000}\n')
      fileHTML.write('             .forumLastPostTd,.forumArchive {font-size:8pt}\n')
      fileHTML.write('             a.catLink {text-decoration:none}\n')
      fileHTML.write('             a.catLink:hover {text-decoration:underline}\n')
      fileHTML.write('             .lastPostGuest,.lastPostUser,.threadAuthor {font-weight:bold}\n')
      fileHTML.write('             .archivedForum{font-size:8pt;color:#FF0000!important;font-weight:bold}\n')
      fileHTML.write('             .forumDescr {font-size:8pt;}\n')
      fileHTML.write('             div.forumModer {color:#999;font-size:8pt}\n')
      fileHTML.write('             .forumModer a {color:#999;text-decoration:underline;}\n')
      fileHTML.write('             .forumModer a:hover {text-decoration:none;}\n')
      fileHTML.write('             .threadFrmLink {color:#999;}\n')
      fileHTML.write('             .forumViewed {font-size:9px}\n')
      fileHTML.write('             .forumBarKw {font-weight:normal}\n')
      fileHTML.write('             a.forumBarA {text-decoration:none;}\n')
      fileHTML.write('             a.forumBarA:hover {text-decoration:none}\n')
      fileHTML.write('             .fastLoginForm {font-size:8pt}\n')
      fileHTML.write('             .switch,.pagesInfo {padding:5px 7px;background:#fff;border:1px solid #ececec;}\n')
      fileHTML.write('             .switchActive {padding:5px 8px;font-size:11px;background:#b2d237;color:#fff;}\n')
      fileHTML.write('             a.switchDigit,a.switchBack,a.switchNext {text-decoration:none;}\n')
      fileHTML.write('             a.switchDigit:hover,a.switchBack:hover,a.switchNext:hover {text-decoration:underline}\n')
      fileHTML.write('             .threadLastPostTd {font-size:8pt}\n')
      fileHTML.write('             .threadDescr {color:#999;font-size:8pt}\n')
      fileHTML.write('             .threadNoticeLink {font-weight:bold}\n')
      fileHTML.write('             .threadsType {height:20px;font-weight:bold;font-size:8pt}\n')
      fileHTML.write('             .threadsDetails {height:20px;font-size:12px;padding:7px 10px;}\n')
      fileHTML.write('             .forumOnlineBar {height:20px;color:#999;padding:0 10px;}\n')
      fileHTML.write('             a.threadPinnedLink {color:#f63333!important}\n')
      fileHTML.write('             .postpSwithces {font-size:8pt;display:block;}\n')
      fileHTML.write('             .thDescr {font-weight:normal}\n')
      fileHTML.write('             .threadFrmBlock {font-size:8pt;text-align:right}\n')
      fileHTML.write('             .forumNamesBar {font-size:11px;padding:3px 0}\n')
      fileHTML.write('             .forumModerBlock {padding:3px 0}\n')
      fileHTML.write('             .postPoll {text-align:center;padding:20px 0!important;}\n')
      fileHTML.write('             .postPoll .pollButtons {padding:10px 0 0;}\n')
      fileHTML.write('             .postUser {font-weight:bold}\n')
      fileHTML.write('             .postRankName {margin-top:5px}\n')
      fileHTML.write('             .postRankIco {margin-bottom:5px;}\n')
      fileHTML.write('             .reputation {margin-top:5px}\n')
      fileHTML.write('             .signatureHr {margin-top:20px}\n')
      fileHTML.write('             .postTdInfo {text-align:center}\n')
      fileHTML.write('             .posttdMessage {line-height:18px;}\n')
      fileHTML.write('             .pollQuestion {text-align:center;font-weight:bold}\n') 
      fileHTML.write('             .pollButtons,.pollTotal {text-align:center}\n')
      fileHTML.write('             .pollSubmitBut,.pollreSultsBut {width:140px;font-size:8pt}\n')
      fileHTML.write('             .pollSubmit {font-weight:bold}\n')
      fileHTML.write('             .pollEnd {text-align:center;height:30px}\n')
      fileHTML.write('             .codeMessage,.quoteMessage,.uSpoilerText {font-size:11px;padding:10px;background:#f5f5f5;border:2px solid #ddd!important;}\n')
      fileHTML.write('             .signatureView {display:block;font-size:8pt;line-height:14px;padding:0 0 0 10px;border-left:3px solid #b2d237;}\n') 
      fileHTML.write('             .edited {padding-top:30px;font-size:8pt;text-align:right;color:gray}\n')
      fileHTML.write('             .editedBy {font-weight:bold;font-size:8pt}\n')
      fileHTML.write('             .statusBlock {padding-top:3px}\n')
      fileHTML.write('             .statusOnline {color:#0f0}\n')
      fileHTML.write('             .statusOffline {color:#f00}\n')
      fileHTML.write('             .newThreadItem {padding:0 0 8px;background:url(/.s/t/1141/12.gif) no-repeat 0 4px}\n')
      fileHTML.write('             .newPollItem {padding:0 0 8px;background:url(/.s/t/1141/12.gif) no-repeat 0 4px}\n')
      fileHTML.write('             .pollHelp {font-weight:normal;font-size:8pt;padding-top:3px}\n')
      fileHTML.write('             .smilesPart {padding-top:5px;text-align:center}\n')
      fileHTML.write('             .pollButtons button {margin:0 10px 0 0!important}\n')
      fileHTML.write('             .postBottom .goOnTop {display:none!important}\n')
      fileHTML.write('             .postIpLink {text-decoration:none;}\n')
      fileHTML.write('             .thread_subscribe {text-decoration:none;}\n')
      fileHTML.write('             .thread_subscribe:hover {text-decoration:underline;}\n')
      fileHTML.write('             .postip,.postip a {font-size:11px;color:#999;}\n')
      fileHTML.write('             .UhideBlockL {background:#f5f5f5;border:2px solid #ddd!important;color:#888;padding:10px;}\n')
      fileHTML.write('             .UhideBlockL a {color:#888;}\n')
      fileHTML.write('             .pollreSultsBut {width:180px;text-align:center;}\n')
      fileHTML.write('             #forum_filter {vertical-align: middle;line-height: 30px;}\n')
      fileHTML.write('             \n')
      fileHTML.write('             #casing input[type="text"],#casing input[type="password"],#casing textarea,#casing input[type="file"],#casing select {margin:0 0 1px;padding:6px 4px;text-align:left;background:#fff;border:2px solid #e6e6e6;color:#000;vertical-align:middle;}\n')
      fileHTML.write('             #casing textarea {height:auto;line-height:normal;padding:6px 4px;resize:vertical;}\n')
      fileHTML.write('             #casing input[type="submit"],#casing input[type="reset"],#casing input[type="button"],#casing button {width:auto!important;cursor:pointer;margin:0 0 1px 1px;text-transform:uppercase;padding:9px 15px;font-weight:normal!important;background:#2B63E8;font-size:11px;color:#fff;border:none;text-transform:uppercase;vertical-align:middle;-webkit-appearance:none;}\n')
      fileHTML.write('             #casing input[type="submit"]:hover,#casing input[type="reset"]:hover,#casing input[type="button"]:hover,#casing button:hover {background:#8da921;}\n')
      fileHTML.write('             #casing .sidebox .schBtn input {width:34px!important;}\n')
      fileHTML.write('             .manTable select {max-width: 300px;}\n')
      fileHTML.write('             .fakefile > input, #uzf > input[type="button"] {height: inherit!important;width:auto!important}\n')
      fileHTML.write('             \n')
      fileHTML.write('             #casing #mchatBtn,#casing .allUsersBtn,#casing .uSearchFlSbm,#iplus input {padding-left:7px!important;padding-right:7px!important;font-size:10px!important;}\n')
      fileHTML.write('             #doSmbBt,.u-combobut {display:none;}\n')
      fileHTML.write('             #casing .u-comboeditcell,#casing .u-combo {border:0!important;background:none!important;}\n')
      fileHTML.write('             #casing .u-combolist,#content .xw-mc,#content .filterBlock {padding:5px 3px;font-size:12px!important;color:#000!important;background:#fff;border:2px solid #e6e6e6;}\n')
      fileHTML.write('             #content .xw-tl,#content .xw-bl,#content .u-menuvsep {display:none;}\n')
      fileHTML.write('             #content .xw-ml,#content .xw-mr {margin:0;padding:0;background:none;}\n')
      fileHTML.write('             #uNetRegF table {text-align:left;}\n')
      fileHTML.write('             #uNetRegF table table {clear:both;}\n')
      fileHTML.write('             #uNetRegF table table td {padding:5px 0 0 0;}\n')
      fileHTML.write('             .sidebox .gTable {background:none;border:none;padding:0;margin:0;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none;}\n')
      fileHTML.write('             .sidebox .gTableTop,.sidebox .gTableSubTop,.sidebox .forumNameTd {border:none;background:none;color:#a9a397;font-weight:normal;text-transform:none;height:auto;line-height:normal;overflow:visible;padding:0;font-size:14px!important;text-transform:none;text-shadow:none;font-family:Tahoma,Geneva,sans-serif;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none;}\n')
      fileHTML.write('             .sidebox .gTable ul {padding:0 0 0 20px;margin:0;width:auto;}\n')
      fileHTML.write('             .sidebox .gTable ul li a {background:none;border:none;padding:5px 0;}\n')
      fileHTML.write('             .sidebox .forumDescr {display:none;}\n')
      fileHTML.write('             .sidebox .gTableTop,.sidebox .gTableSubTop {display:block;color:#000;margin:0 0 1px;padding:5px 0!important;text-decoration:none;border:none;}\n')
      fileHTML.write('             .sidebox .gTableTop:hover,.sidebox .gTableSubTop:hover,.sidebox .gTable ul li a:hover {color:#000;padding:5px 0!important;}\n')
      fileHTML.write('             .sidebox .gTableTop:hover:after,.sidebox .gTableSubTop:hover:after,.sidebox .gTable ul li a:hover:after {content:"\\2022";font-size:14px;font-family:Tahoma,Geneva,sans-serif;padding:0 0 0 8px;color:#8aae01;}\n')
      fileHTML.write('             .sidebox .gTableTop:before,.sidebox .gTableSubTop:before {content:"\\002B";font-size:16px;font-family:Tahoma,Geneva,sans-serif;color:#b2b2b2;padding:0 5px 0 0;}\n')
      fileHTML.write('             .manTable td input,.manTable td textarea {max-width:99%;}\n')
      fileHTML.write('             .manTable td input#id_file_add {max-width:none;}\n')
      fileHTML.write('             input[id$="basket"] {text-align:center!important;}\n')
      fileHTML.write('             #content .postRest2:first-child,#content .postRest1:first-child {text-align:center;}\n')
      fileHTML.write('             #thread_search_field {max-width:65%;margin:0 0 2px!important;}\n')
      fileHTML.write('             \n')
      fileHTML.write('             \n')
      fileHTML.write('             \n')
      fileHTML.write('             #catmenu.nav-mobi {padding:0 20px;width:auto;height:auto;max-width:none;margin:0 auto;float:none;padding:0;border:none;text-align:left;max-width:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none;}\n')
      fileHTML.write('             #catmenu.nav-mobi .nav-head {display:none;cursor:pointer;text-transform:uppercase;font-size:20px;text-align:left;margin:0 auto;padding:20px;background:#8da921;color:#fff;}\n')
      fileHTML.write('             .nav-head a {color:#fff;text-decoration:none; }\n')
      fileHTML.write('             .nav-head div.icon {float:right;width:40px;margin:2px 0 0;}\n')
      fileHTML.write('             .nav-head div.icon span {display:block;background:#fff;height:4px;margin:0 0 2px;}\n')
      fileHTML.write('             .nav-head:hover a,.nav-head.active a,.nav-head.over a {color:#fff;}\n')
      fileHTML.write('             .nav-head:hover div.icon span,.nav-head.active div.icon span,.nav-head.over div.icon span {background:#fff;}\n')
      fileHTML.write('             #catmenu.nav-mobi li a:before,#catmenu.nav-mobi li a:after,#catmenu.nav-mobi li a.uMenuItemA:hover:before,#catmenu.nav-mobi li a.uMenuItemA:hover:after {display:none!important;}\n')
      fileHTML.write('             #catmenu.nav-mobi li a.uMenuItemA {background:#748b19;}\n')
      fileHTML.write('             \n')
      fileHTML.write('             #catmenu.nav-mobi ul {display:none;padding:0;position:relative;border:none;float:none;margin:0;width:auto;height:auto;overflow:visible;background:none;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul ul {background:#fff;padding:0;top:0;left:0;z-index:999;width:auto;margin:0!important;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul ul ul {margin:0!important;border:none;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li {text-align:left;height:auto;float:none;position:relative;display:block;padding:0;text-transform:uppercase;border:none!important;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li.item-parent {position:relative!important;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li li {padding:0;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li.over {z-index:998;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li a {font-size:13px;display:block;border:none;color:#fff;height:auto;width:auto!important;line-height:normal;text-decoration:none;float:none;padding:0!important;border-top:1px solid #b2d237;background:#8da921;-moz-border-radius:0;-webkit-border-radius:0;border-radius:0;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li.over > a {background:#748b19;color:#fff;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li.over > em {color:#fff;}\n')
      fileHTML.write('             #catmenu.nav-mobi li.item-parent a {background-image:none!important;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li li a {font-size:11px;color:#fff;background:#8da921;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li li li a {background:#8da921;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li a:hover {text-decoration:none;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li a span {text-align:left;display:block;white-space:nowrap;cursor:pointer;padding:0 20px;line-height:40px;height:40px;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li ul a span {white-space:normal;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li em {position:absolute;display:block;border-left:1px solid #b2d237;color:#fff;top:1px;right:0;width:40px;line-height:40px;height:40px;text-align:center;font-style:normal;font-size:13px;font-weight:bold;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul li em:hover,#catmenu.nav-mobi ul>li>a:hover {cursor:pointer;color:#fff!important;background:#748b19!important;}\n')
      fileHTML.write('             #catmenu.nav-mobi ul>li>a:hover>span,\n')
      fileHTML.write('             #catmenu.nav-mobi ul>li.over>a>span,\n')
      fileHTML.write('             #catmenu.nav-mobi ul>li.active>a>span{border:none;}\n')
      fileHTML.write('             \n')
      fileHTML.write('             .vep-video-block img {max-width: 100%;}\n')
      fileHTML.write('             \n')
      fileHTML.write('             /***** Standard 1200px *****/\n')
      fileHTML.write('             .wrapper {width:1180px;}\n')
      fileHTML.write('             \n')
      fileHTML.write('             /***** Standard 960px *****/\n')
      fileHTML.write('             @media only screen and (min-width:960px) and (max-width:1200px) {\n')
      fileHTML.write('             .wrapper {width:960px;}\n')
      fileHTML.write('             #promo {padding:0 40px 60px;}\n')
      fileHTML.write('             .promo-ttl {font-size:36px;margin:140px 0 20px;}\n')
      fileHTML.write('             .promo-txt {font-size:13px;}\n')
      fileHTML.write('             }\n')
      fileHTML.write('             \n')
      fileHTML.write('             @media only screen and (max-width: 960px) { \n')
      fileHTML.write('             .navbar-share {display: none;}\n')
      fileHTML.write('             }\n')
      fileHTML.write('             \n')
      fileHTML.write('             /***** iPad Smaller than 959px *****/\n')
      fileHTML.write('             @media only screen and (min-width:768px) and (max-width:959px) { \n')
      fileHTML.write('             .wrapper {width:768px;}\n')
      fileHTML.write('             #promo {padding:0 40px 40px;}\n')
      fileHTML.write('             .promo-ttl {font-size:30px;margin:100px 0 20px;}\n')
      fileHTML.write('             .promo-txt {font-size:13px;}\n')
      fileHTML.write('             #catmenu,#soc-box {float:none;width:auto;text-align:center;}\n')
      fileHTML.write('             #soc-box a {margin:0 5px;}\n')
      fileHTML.write('             #content,#sidebar {float:none;width:auto;}\n')
      fileHTML.write('             #content {padding:0 0 40px;}\n')
      fileHTML.write('             .big-img {margin:50px 0;}\n')
      fileHTML.write('             .big-img:before {\n')
      fileHTML.write('              height:65px;top:-30px;}\n')
      fileHTML.write('             .big-img:after {\n')
      fileHTML.write('              height:65px;bottom:-30px;}\n')
      fileHTML.write('             }\n')
      fileHTML.write('             /***** iPhone (portrait) *****/\n')
      fileHTML.write('             @media only screen and (max-width:767px) {\n')
      fileHTML.write('             .wrapper {width:300px;}\n')
      fileHTML.write('             #header {background-image:none;}\n')
      fileHTML.write('             #header-i {padding:0;}\n')
      fileHTML.write('             #site-logo {padding:40px 0;text-align:center;}\n')
      fileHTML.write('             .site-l {overflow:visible;padding:0;}\n')
      fileHTML.write('             .site-l:before,.site-l:after {display:none;}\n')
      fileHTML.write('             .site-n {background:none;padding:0;font-size:20px;}\n')
      fileHTML.write('             #promo {display:none;}\n')
      fileHTML.write('             #nav-box {padding:0 0 20px;}\n')
      fileHTML.write('             #catmenu.nav-mobi .nav-head {display:block;}\n')
      fileHTML.write('             #soc-box {float:none;width:auto;text-align:center;}\n')
      fileHTML.write('             #content,#sidebar {float:none;width:auto;}\n')
      fileHTML.write('             #content {padding:0 0 20px;}\n')
      fileHTML.write('             .eTitle,.eBlock .eTitle,.eBlock td.eTitle {font-size:22px;}\n')
      fileHTML.write('             .eDetails,.eDetails1,.eDetails2,.eBlock td.eDetails,.eBlock td.eDetails1,.eBlock td.eDetails2 {margin:0 0 1px!important;}\n')
      fileHTML.write('             .eDetails:before,.eDetails1:before,.eDetails:after,.eDetails1:after,.eDetails2:after,.eDetails2:before {display:none;}\n')
      fileHTML.write('             .eBlock td.eMessage,.eBlock td.eText,.eMessage,.eText {padding:20px 0!important;}\n')
      fileHTML.write('             .eMessage img,.eText img {width:294px;float:none;margin:0 0 15px!important;}\n')
      fileHTML.write('             #footer {font-size:11px;}\n')
      fileHTML.write('             .manTable td {display:block;width:100%;}\n')
      fileHTML.write('             .manTable td input,.manTable td textarea {max-width:97%;}\n')
      fileHTML.write('             #uNetRegF tr td:first-child {max-width:20%!important;white-space:normal!important;font-size:9px;}\n')
      fileHTML.write('             #uNetRegF #fAvatar,#uNetRegF #fAvatarU {display:block;margin:0 0 3px;}\n')
      fileHTML.write('             #uNetRegF #fAvatarU + input {position:relative;margin:0 0 0 -10px;}\n')
      fileHTML.write('             #uNetRegF input,#uNetRegF select,#uNetRegF input[type="file"] {max-width:162px;}\n')
      fileHTML.write('             .uNetDescr {font-size:9px;}\n')
      fileHTML.write('             #fTerms+label {font-size:9px!important;}\n')
      fileHTML.write('             #fTerms~div {font-size:9px;padding:10px 0 0;}\n')
      fileHTML.write('             .copy {font-size:9px;}\n')
      fileHTML.write('             .calendarsTable,.calendarsTable > tbody,.calendarsTable > tbody > tr,.calendarsTable > tbody > tr > td {display:block;width:100%;}\n')
      fileHTML.write('             #content .calTable {width:100%;margin:0 0 20px;}\n')
      fileHTML.write('             #content .calMonth {text-align:center;}\n')
      fileHTML.write('             .forum-box .gTableSubTop,.forum-box .forumIcoTd,.forum-box .forumThreadTd,.forum-box .forumPostTd,.forum-box .forumLastPostTd,.forum-box .threadIcoTd,.forum-box .threadPostTd,.forum-box .threadViewTd,.forum-box .threadAuthTd,.forum-box .threadLastPostTd,.forum-box .legendTable,.forum-box .fFastSearchTd,.forum-box .fFastNavTd,.forum-box .funcBlock,.forum-box .userRights,.forum-box .forumNamesBar{display:none;}\n')
      fileHTML.write('             .forum-box .gTableTop {padding:10px;}\n')
      fileHTML.write('             .forum-box .gTable td.forumNameTd,.forum-box .gTable td.threadNametd,.forum-box .postTable,.forum-box .postTable tbody,.forum-box .postTable tr,.forum-box .postTable td {display:block;width:auto!important;}\n')
      fileHTML.write('             .forum-box td.postBottom,.forum-box td.postTdInfo {display:none;}\n')
      fileHTML.write('             .forum-box .postTdTop {text-align:left;font-size:9px;position:relative;margin:0 0 -6px;-moz-box-shadow:none;-webkit-box-shadow:none;box-shadow:none;}\n')
      fileHTML.write('             .forum-box .postTdTop:first-child {-moz-border-radius:0;-webkit-border-radius:0;border-radius:0;}\n')
      fileHTML.write('             .forum-box .postTdTop + .postTdTop {margin:5px 0 2px;}\n')
      fileHTML.write('             .forum-box .postTdTop + .postTdTop:before {content:"";width:0;height:0;border-top:7px solid #e6e6e6;border-left:10px solid transparent;border-right:10px solid transparent;position:absolute;bottom:-7px;left:40px;}\n')
      fileHTML.write('             .fNavLink {font-size:9px;position:relative;margin:0 -3px;}\n')
      fileHTML.write('             .codeButtons,.smilesPart {display:none;}\n')
      fileHTML.write('             .edtTypeMenu{display: none;}\n')
      fileHTML.write('             #message {max-width:97%;}\n')
      fileHTML.write('             .postUser {font-size:14px;}\n')
      fileHTML.write('             #frM53 .gTableLeft,#frM53 .gTableRight {display:block;width:auto!important}\n')
      fileHTML.write('             .uTable tr td:first-child + td ~ td {display:none;}\n')
      fileHTML.write('             .uTd .user_avatar img {width:40px;}\n')
      fileHTML.write('             .opt_vals td {display:table-cell!important;}\n')
      fileHTML.write('             .opt_items {max-width:97%;}\n')
      fileHTML.write('             #puzadpn {display:none;}\n')
      fileHTML.write('             #uEntriesList .uEntryWrap {margin:0 5px 10px;width:auto!important;}\n')
      fileHTML.write('             .shop-tabs {border-bottom: 0!important;}\n')
      fileHTML.write('             .shop-tabs li {border-bottom: 1px solid #A7A6A6 !important;}\n')
      fileHTML.write('             }\n')
      fileHTML.write('             /***** iPhone (landscape) *****/\n')
      fileHTML.write('             @media only screen and (min-width:480px) and (max-width:767px) {\n')
      fileHTML.write('             .wrapper {width:456px;}\n')
      fileHTML.write('             .site-n {font-size:30px;}\n')
      fileHTML.write('             #content {padding:0 0 40px;}\n')
      fileHTML.write('             .eMessage img,.eText img {width:450px;}\n')
      fileHTML.write('             }\n')
      fileHTML.write('             .entTd .eDetails {margin:0 0 40px;}\n')
      fileHTML.write('             #thread_search_field {max-width:65%;margin:0 0 2px!important;}\n')
      fileHTML.write('             .gTable select {margin:0 0 2px;}\n')
      fileHTML.write('             .opt_vals .gTableSubTop {padding-left:0;background:none;}\n')
      fileHTML.write('             #content form[action$="search/"] table {width:100%;}\n')
      fileHTML.write('             #content form[action$="search/"] table td {white-space:normal!important;}\n')
      fileHTML.write('             #content form[action$="search/"] table td+td {width:30%;}\n')
      fileHTML.write('             #content .queryField {width:70%!important;}\n')
      fileHTML.write('             #slideshowBlock7 {margin:0 0 20px;}\n')
      fileHTML.write('        </style>\n')
      fileHTML.write('		<script type="text/javascript">\n')
      fileHTML.write('		    var browser = navigator.userAgent;\n')
      fileHTML.write('		    var browserRegex = /(Android|BlackBerry|IEMobile|Nokia|iP(ad|hone|od)|Opera M(obi|ini))/;\n')
      fileHTML.write('		    var isMobile = false;\n')
      fileHTML.write('		    if(browser.match(browserRegex)){\n')
      fileHTML.write('		        isMobile = true;\n')
      fileHTML.write('		        addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false);\n')
      fileHTML.write('		        function hideURLbar(){\n')
      fileHTML.write('		            window.scrollTo(0,1);\n')
      fileHTML.write('		        }\n')
      fileHTML.write('		    }\n')
      fileHTML.write('		</script>\n')
      fileHTML.write('	</head>\n')
      fileHTML.write('	<body>\n')
      fileHTML.write('	    <header>\n')
      fileHTML.write('	        <div id="header">\n')
      fileHTML.write('	            <div id="header-i">\n')
      fileHTML.write('	                <div class="wrapper">\n')
      fileHTML.write('	                    <div id="site-logo">\n')
      fileHTML.write('	                        <span class="site-l">\n')
      fileHTML.write('	                            <span class="site-n">\n')
      fileHTML.write('	                                <a href="http://tpm.docmase.lucadistasioengineering.com/">DocMASE Project 2015-04</a>\n')
      fileHTML.write('	                            </span>\n')
      fileHTML.write('	                        </span>\n')
      fileHTML.write('	                    </div>\n')
      fileHTML.write('	                    <div id="promo">\n')
      fileHTML.write('	                        <div class="promo-ttl">Mechanics of Extreme Thin Composite Layers for Aerospace Applications</div>\n')
      tempstring = ''
      tempstring = '	                        <div class="promo-txt"><a href="http://www.eeigm.univ-lorraine.fr/">Ecole Européenne d’Ingénieurs en Génie des Matériaux</a><br><a href="http://www.univ-lorraine.fr/">Université de Lorraine</a></div>\n'
      fileHTML.write(tempstring.decode('utf-8'))
      tempstring = ''
      tempstring = '	                        <div class="promo-txt"><a href="http://www.ltu.se/org/tvm?l=en">Department of Engineering Sciences and Mathematics</a><br><a href="http://www.ltu.se/?l=en">Luleå University of Technology</a> </div>\n'
      fileHTML.write(tempstring.decode('utf-8'))
      fileHTML.write('	                    </div>\n')
      fileHTML.write('	                </div>\n')
      fileHTML.write('	            </div>\n')
      fileHTML.write('	        </div>\n')
      fileHTML.write('	    </header>\n')
      fileHTML.write('	    <nav>\n')
      fileHTML.write('	        <div id="nav-box">\n')
      fileHTML.write('	            <div class="wrapper">\n')
      fileHTML.write('	                <div id="soc-box">\n')
      fileHTML.write('	                    <a href="https://www.facebook.com/tpm.docmase?ref=hl" class="soc-fc" target="_blank"></a>\n')
      fileHTML.write('	                </div>\n')
      fileHTML.write('	                <div id="catmenu">\n')
      fileHTML.write('	                    <div id="uNMenuDiv1" class="uMenuV">\n')
      fileHTML.write('	                        <ul class="uMenuRoot">\n')
      fileHTML.write('	                            <li><a class=" uMenuItemA" href="/"><span>Home page</span></a></li>\n')
      fileHTML.write('	                            <li><a href="/about"><span>About</span></a></li>\n')
      fileHTML.write('	                            <li><a href="/project"><span>Project</span></a></li>\n')
      fileHTML.write('	                            <li><a href="/links"><span>Resources</span></a></li>\n')
      fileHTML.write('	                            <li><a href="/links"><span>Dashboard</span></a></li>\n')
      fileHTML.write('	                            <li><a href="/contacts"><span>Contacts</span></a></li>\n')
      fileHTML.write('	                        </ul>\n')
      fileHTML.write('	                    </div>\n')
      fileHTML.write('	                    <div class="clr"></div>\n')
      fileHTML.write('	               </div>\n')
      fileHTML.write('	                <div class="clr"></div>\n')
      fileHTML.write('	            </div>\n')
      fileHTML.write('	        </div>\n')
      fileHTML.write('	    </nav>\n')
      fileHTML.write('	    <div id="main">\n')
      fileHTML.write('            <div class="wrapper">\n')
      fileHTML.write('                <div id="content" >\n')
      fileHTML.write('                    <section>\n')
      fileHTML.write('                        <div id="nativeroll_video_cont" style="display:none;">\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                        <div id="database_header">\n')
      fileHTML.write('		                       <h1> Thematic analysis of scientific literature</h1>\n')
      fileHTML.write('		                       <h2> Database of references</h2>\n')
      fileHTML.write('		                       <h3> Source: <source>mendeley<source></h3>\n')
      fileHTML.write('		                       <h3> Query: <query>' + string + '<query></h3>\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                        <div id="database_items">\n')
      fileHTML.write('                          <div class="database_entry">\n')
      fileHTML.write('                          </div>\n')
      fileHTML.write('                        <!-- INSERT NEW ELEMENT HERE -->\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                    </section>\n')
      fileHTML.write('                </div>\n')
      fileHTML.write('                <aside>\n')
      fileHTML.write('                    <div id="sidebar">\n')
      fileHTML.write('                        <div class="big-box">\n')
      fileHTML.write('                            <div class="big-ttl">\n')
      fileHTML.write('                                <span></span>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="big-img">\n')
      fileHTML.write('                                <img src="http://docmase.ucoz.com/Docmase_logo.jpg" border="0" alt="" />\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="inner">\n')
      fileHTML.write('                                <div class="wel-txt">\n')
      fileHTML.write('                                    <span>Welcome, <b>Guest</b>!</span>\n')
      fileHTML.write('                                </div>\n')
      fileHTML.write('                                <div class="wel-lnk">\n')
      fileHTML.write('                                    <a title="Sign Up" href="/register">Sign Up</a> | <a title="Log In" href="javascript://" rel="nofollow" onclick="new _uWnd("LF"," ",-250,-110,{autosize:1,closeonesc:1,resize:1},{url:"/index/40"});return false;">Log In</a>\n')
      fileHTML.write('                                </div>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="clr"></div>\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                        <div class="sidebox">\n')
      fileHTML.write('                            <div class="sidetitle">\n')
      fileHTML.write('                                <span>Log In</span>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="inner">\n')
      fileHTML.write('                                <div id="uidLogForm" align="center">\n')
      fileHTML.write('                                    <a href="javascript://" onclick="window.open("http://login.uid.me/?site=ddocmase&amp;ref="+escape(location.protocol + "//" + ("docmase.ucoz.com" || location.hostname) + location.pathname + ((location.hash ? ( location.search ? location.search + "&" : "?" ) + "rnd=" + Date.now() + location.hash : ( location.search || '' )))),"unetLoginWnd","width=500,height=350,resizable=yes,titlebar=yes");return false;" class="login-with uid" title="Log in with uID" rel="nofollow"><i></i></a><a href="javascript://" onclick="return uSocialLogin("facebook");" class="login-with facebook" title="Log in with Facebook" rel="nofollow"><i></i></a><a href="javascript://" onclick="return uSocialLogin("google");" class="login-with google" title="Log in with Google+" rel="nofollow"><i></i></a><a href="javascript://" onclick="return uSocialLogin("twitter");" class="login-with twitter" title="Log in with Twitter" rel="nofollow"><i></i></a>\n')
      fileHTML.write('                                </div>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="clr"></div>\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                        <div class="sidebox">\n')
      fileHTML.write('                            <div class="sidetitle">\n')
      fileHTML.write('                                <span>Search</span>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="inner">\n')
      fileHTML.write('                                <div align="center">\n')
      fileHTML.write('                                    <div class="searchForm">\n')
      fileHTML.write('                                        <form onsubmit="this.sfSbm.disabled=true" method="get" style="margin:0" action="/search/">\n')
      fileHTML.write('                                            <div align="center" class="schQuery"><input type="text" name="q" maxlength="30" size="20" class="queryField" />\n')
      fileHTML.write('                                            </div>\n')
      fileHTML.write('                                            <div align="center" class="schBtn"><input type="submit" class="searchSbmFl" name="sfSbm" value="Search" />\n')
      fileHTML.write('                                            </div>\n')
      fileHTML.write('                                        </form>\n')
      fileHTML.write('                                    </div>\n')
      fileHTML.write('                                </div>\n')   
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="clr"></div>\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                        <div class="sidebox">\n')
      fileHTML.write('                            <div class="sidetitle">\n')
      fileHTML.write('                                <span>Calendar</span>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="inner">\n')
      fileHTML.write('                                <div align="center">\n')
      fileHTML.write('                                    <!-- Calendar begins -->\n')
      fileHTML.write('                                    <table border="0" cellspacing="1" cellpadding="2" class="calTable">\n')
      fileHTML.write('                                        <tr>\n')
      fileHTML.write('                                            <td align="center" class="calMonth" colspan="7"><a title="December 2015" class="calMonthLink" href="javascript://" rel="nofollow" onclick="window.location.href=""+atob("aHR0cDovL2RvY21hc2UudWNvei5jb20vbmV3cy8=")+"2015-12";return false;">&laquo;</a>&nbsp; <a class="calMonthLink" href="javascript://" rel="nofollow" onclick="window.location.href=''+atob("aHR0cDovL2RvY21hc2UudWNvei5jb20vbmV3cy8=")+"2016-01";return false;">January 2016</a> &nbsp;<a title="February 2016" class="calMonthLink" href="javascript://" rel="nofollow" onclick="window.location.href=''+atob("aHR0cDovL2RvY21hc2UudWNvei5jb20vbmV3cy8=")+"2016-02";return false;">&raquo;</a></td>\n')
      fileHTML.write('                                        </tr>\n')
      fileHTML.write('                                        <tr>\n')
      fileHTML.write('                                            <td align="center" class="calWdaySu">Su</td><td align="center" class="calWday">Mo</td><td align="center" class="calWday">Tu</td><td align="center" class="calWday">We</td><td align="center" class="calWday">Th</td><td align="center" class="calWday">Fr</td><td align="center" class="calWdaySe">Sa</td>\n')
      fileHTML.write('                                        </tr>\n')
      fileHTML.write('                                        <tr>\n')
      fileHTML.write('                                            <td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td align="center" class="calMday">1</td><td align="center" class="calMday">2</td></tr>\n')
      fileHTML.write('                                        <tr>\n')
      fileHTML.write('                                            <td align="center" class="calMday">3</td><td align="center" class="calMday">4</td><td align="center" class="calMday">5</td><td align="center" class="calMday">6</td><td align="center" class="calMday">7</td><td align="center" class="calMday">8</td><td align="center" class="calMday">9</td>\n')
      fileHTML.write('                                        </tr>\n')
      fileHTML.write('                                        <tr>\n')
      fileHTML.write('                                            <td align="center" class="calMday">10</td><td align="center" class="calMday">11</td><td align="center" class="calMday">12</td><td align="center" class="calMday">13</td><td align="center" class="calMday">14</td><td align="center" class="calMday">15</td><td align="center" class="calMday">16</td>\n')
      fileHTML.write('                                        </tr>\n')
      fileHTML.write('                                        <tr>\n')
      fileHTML.write('                                            <td align="center" class="calMday">17</td><td align="center" class="calMday">18</td><td align="center" class="calMday">19</td><td align="center" class="calMday">20</td><td align="center" class="calMdayA">21</td><td align="center" class="calMday">22</td><td align="center" class="calMday">23</td>\n')
      fileHTML.write('                                        </tr>\n')
      fileHTML.write('                                        <tr>\n')
      fileHTML.write('                                            <td align="center" class="calMday">24</td><td align="center" class="calMday">25</td><td align="center" class="calMday">26</td><td align="center" class="calMday">27</td><td align="center" class="calMday">28</td><td align="center" class="calMday">29</td><td align="center" class="calMday">30</td>\n')
      fileHTML.write('                                        </tr>\n')
      fileHTML.write('                                        <tr>\n')
      fileHTML.write('                                            <td align="center" class="calMday">31</td>\n')
      fileHTML.write('                                        </tr>\n')
      fileHTML.write('                                    </table>\n')
      fileHTML.write('                                    <!-- Calendar ends -->\n')
      fileHTML.write('                                </div>\n')  
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="clr"></div>\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                        <div class="sidebox">\n')
      fileHTML.write('                            <div class="sidetitle">\n')
      fileHTML.write('                                <span>Useful Links</span>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="inner">\n')
      fileHTML.write('                                <li><a href="http://www.uni-saarland.de/einrichtung/eusmat.html" target="_blank" class="noun">EUSMAT Home</a></li>\n')
      fileHTML.write('                                <li><a href="http://www.uni-saarland.de/einrichtung/eusmat/international-studies/phd/docmase.html" target="_blank" class="noun">DocMASE Home</a></li>\n')
      fileHTML.write('                                <li><a href="http://www.eeigm.univ-lorraine.fr/" target="_blank" class="noun">EEIGM Home</a></li>\n')
      fileHTML.write('                                <li><a href="http://eacea.ec.europa.eu/erasmus_mundus/index_en.php" target="_blank" class="noun">Erasmus Mundus Home</a></li>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="clr"></div>\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                        <div class="sidebox">\n')
      fileHTML.write('                            <div class="sidetitle">\n')
      fileHTML.write('                                <span>Statistics</span>\n')
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="inner">\n')
      fileHTML.write('                                <div align="center">\n')
      fileHTML.write('                                    <hr />\n')
      fileHTML.write('                                    <div class="tOnline" id="onl1">Total online: <b>0</b></div>\n')
      fileHTML.write('                                    <div class="gOnline" id="onl2">Guests: <b>0</b></div>\n')
      fileHTML.write('                                    <div class="uOnline" id="onl3">Users: <b>0</b></div>\n')
      fileHTML.write('                                </div>\n')  
      fileHTML.write('                            </div>\n')
      fileHTML.write('                            <div class="clr"></div>\n')
      fileHTML.write('                        </div>\n')
      fileHTML.write('                    </div>\n')
      fileHTML.write('                </aside>\n')
      fileHTML.write('                <div class="clr"></div>\n')
      fileHTML.write('            </div>\n')
      fileHTML.write('        </div>\n')
      fileHTML.write('        <footer>\n')
      fileHTML.write('            <div class="wrapper">\n')
      fileHTML.write('                <div id="footer">&copy; 2016 Luca Di Stasio | <span class="pbzSJDTb"><a href="http://www.ucoz.com/" title="Website created with uCoz" target="_blank" rel="nofollow">uCoz</a></span>\n')
      fileHTML.write('                </div>\n')
      fileHTML.write('	        </div>\n')
      fileHTML.write('	    </footer>\n')
      fileHTML.write('	</body>\n')
      fileHTML.write('</html>\n')
    
    
   websites= {1:'https://www.google.com',
              2:'https://www.facebook.com/',
              3:'https://www.linkedin.com/',
              4:'https://www.researchgate.net/home',
              5:'http://www.polimi.it/',
              6:'https://www.ethz.ch/de.html',
              7:'http://www.drexel.edu/',
              8:'https://www.youtube.com/',
              9:'http://www.univ-lorraine.fr/',
              10:'https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal',
              11:'http://physics.wustl.edu/nd/event/qmcd09/Docs/intro.php',
              12:'http://www.tre.it/',
              13:'https://www1.sunrise.ch/',
              14:'http://moocs.epfl.ch/information',
              15:'http://www.epfl.ch/',
              16:'http://www.lemonde.fr/',
              17:'http://www.ilgiornale.it/',
              18:'http://www.corriere.it/',
              19:'http://www.larousse.fr/dictionnaires/francais',
              20:'https://www.blablacar.fr/'}
   
   # Browser
   mech = mechanize.Browser()
   
   # Enable cookie support for urllib2 
   cookiejar = cookielib.LWPCookieJar() 
   mech.set_cookiejar( cookiejar )
   
   # Broser options 
   mech.set_handle_equiv( True ) 
   mech.set_handle_gzip( True ) 
   mech.set_handle_redirect( True ) 
   mech.set_handle_referer( True ) 
   mech.set_handle_robots( False ) 
   mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
   
   mech.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'),
                              ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                              ('Accept-Language', 'en-gb,en;q=0.5'),
                              ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
                              ('Proxy-Connection', 'keep-alive')]
   
   secondmech = mechanize.Browser()
   
   # Enable cookie support for urllib2 
   secondcookiejar = cookielib.LWPCookieJar() 
   secondmech.set_cookiejar( secondcookiejar )
   
   # Broser options 
   secondmech.set_handle_equiv( True ) 
   secondmech.set_handle_gzip( True ) 
   secondmech.set_handle_redirect( True ) 
   secondmech.set_handle_referer( True ) 
   secondmech.set_handle_robots( False ) 
   secondmech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
   
   secondmech.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'),
                              ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                              ('Accept-Language', 'en-gb,en;q=0.5'),
                              ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
                              ('Proxy-Connection', 'keep-alive')]
   #Configuring Proxies
   #br.set_proxies({'http':'127.0.0.1:8120'})

   # Create url for the query
   query = url + string.replace(" ","+")
   
   main = mech.open(query)
   html = main.read()
   #with open("mendeley_search.html","w") as htmlfile:
   #   htmlfile.write(html)
   initmainsoup = BeautifulSoup(html)
   
   count = 0
   
   if startpage==0:
      page = 0
   else:
      page = startpage   
   
   pageitems = initmainsoup.body.find(id="wrapper").find(id="main-container").find(id="content-container").find(id="main-content").find('div',"pagemenu").ul.findAll('li')
   maxpage = pageitems[-1].text
   g = re.search('[0-9.]+', maxpage)  # capture the inner number only
   maxpage = g.group(0)
   
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"
   print "                           PUBLICATIONS"
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"
   
   while page < int(maxpage):
      pagequery = query + "&page=" + str(page)
      page = page + 1
      selectbrowser = 1 # Chrome
      if randint(0,100) > 50:
         selectbrowser = 0 # Firefox
      if selectbrowser:
         pagemain = mech.open(pagequery)
      else:
         pagemain = secondmech.open(pagequery)
      pagehtml = pagemain.read().decode('utf-8', 'ignore')
      mainsoup = BeautifulSoup(pagehtml)
      if mainsoup.body.find(id="wrapper").find(id="main-container").find(id="content-container").find(id="main-content").find('ol') != None:
         for item in mainsoup.body.find(id="wrapper").find(id="main-container").find(id="content-container").find(id="main-content").find('ol').findAll('li'):
            pubs = []
            title = ""
            link = ""
            authors = ""
            publication = ""
            year = ""
            volume = ""
            issue = ""
            pages = ""
            doi = ""
            abstract = ""
            keywords = ""
            count = count + 1
            title = item.article.find('div',"item-info").find('div',"title").a.get("title")
            link = item.article.find('div',"item-info").find('div',"title").a.get("href").encode('utf8')
            for author in item.article.find('div',"item-info").find('div',"metadata").find('span',"authors").findAll('span',"author"):
               newauthor = author.text
               if authors != "":
                  authors = authors + ", " + newauthor
               else:
                  authors = authors + newauthor
            publication = item.article.find('div',"item-info").find('div',"metadata").find('span',"publication").text
            year = str(item.article.find('div',"item-info").find('div',"metadata").find('span',"year").text).replace("(","").replace(")","")
            itemurl = "https://www.mendeley.com" + link
            if selectbrowser:
               itempage = mech.open(itemurl)
            else:
               itempage = secondmech.open(itemurl)
            itemhtml = itempage.read().decode('utf-8', 'ignore')
            itemsoup = BeautifulSoup(itemhtml)
            if itemsoup.body.find('article').find(id="abstract-container") != None:
               abstract = itemsoup.body.find('article').find(id="abstract-container").p.text
            if itemsoup.body.find('article').find('ul',"identifiers-list") != None:
               for identifier in itemsoup.body.find('article').find('ul',"identifiers-list").findAll('li'):
                  if "DOI" in identifier.span.text or "doi" in identifier.span.text:
                     doi = identifier.a.text
            if itemsoup.body.find('article').find('div',"container-metadata") != None:
               for info in itemsoup.body.find('article').find('div',"container-metadata").findAll('span',"info"):
                  if "volume" in info.text or "Volume" in info.text:
                     volume = info.span.text
                  elif "issue" in info.text or "Issue" in info.text:
                     issue = info.span.text
                  elif "pages" in info.text or "Pages" in info.text:
                     pages = info.span.text
            if itemsoup.body.find('article').find(id="keywords-container") != None:
               for keyword in itemsoup.body.find('article').find(id="keywords-container").find('div',"tags-list").findAll('a',"tag"):
                  newkeyword = keyword.text
                  if keywords != "":
                     keywords = keywords + "; " + newkeyword
                  else:
                     keywords = keywords + newkeyword
         
            pubs = [title, authors, publication, volume, issue, pages, year, doi, abstract, keywords]
            if selectbrowser:
               browser = "Chrome on Windows 7 64 bit"
            else:
               browser = "Firefox on Windows 7 64 bit"
            print "----------------------------------------------------------------------"
            print "PUBLICATION number " + str(count) + " out of " + maxpage + " retrieved using " + browser + " on " + str(datetime.now().day) + "/" + str(datetime.now().month) + "/" + str(datetime.now().year) + " at " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
            print ""
            print pubs[0]
            print pubs[1]
            print pubs[2] + ' (' + pubs[6] + '), volume ' + pubs[3] + ', issue ' + pubs[4] + ', page(s) ' + pubs[5]
            print ""
            print "DOI: http://www.doi.org/" + pubs[7]
            print ""
            print pubs[8]
            print ""
            print pubs[9]
            print "----------------------------------------------------------------------"
            
            lines = []
            with codecs.open(pathHTML,'r','utf-8') as fileHTML:
               for line in fileHTML.readlines():
                  if "<!-- INSERT NEW ELEMENT HERE -->" in line:
                     lines.append('                          <div class="database-entry">\n')
                     lines.append('                            <div class="item-info">\n')
                     if title != "":
                        lines.append('                               <div class="item-title">\n')
                        lines.append('                                  <span>\n')
                        lines.append('                                     ' + title + '\n')
                        lines.append('                                  <span>\n')
                        lines.append('                               </div>\n')
                     lines.append('                               <div class="metadata">\n')
                     if authors != "":
                        lines.append('                                  <div class="authors">\n')
                        lines.append('                                     <span>\n')
                        lines.append('                                        ' + authors + '\n')
                        lines.append('                                     </span>\n')
                        lines.append('                                  </div>\n')
                     if publication != "":
                        lines.append('                                  <div class="publication">\n')
                        lines.append('                                     <span>\n')
                        lines.append('                                        ' + publication + '\n')
                        lines.append('                                     </span>\n')
                        lines.append('                                  </div>\n')
                     if volume != "":
                        lines.append('                                  <div class="volume">\n')
                        lines.append('                                     <span>\n')
                        lines.append('                                        Volume ' + volume + '\n')
                        lines.append('                                     </span>\n')
                        lines.append('                                  </div>\n')
                     if issue != "":
                        lines.append('                                  <div class="issue">\n')
                        lines.append('                                     <span>\n')
                        lines.append('                                        Issue ' + issue + '\n')
                        lines.append('                                     </span>\n')
                        lines.append('                                  </div>\n')
                     if pages != "":
                        lines.append('                                  <div class="pages">\n')
                        lines.append('                                     <span>\n')
                        lines.append('                                        Page(s) ' + pages + '\n')
                        lines.append('                                     </span>\n')
                        lines.append('                                  </div>\n')
                     if year != "":
                        lines.append('                                  <div class="year">\n')
                        lines.append('                                     <span>\n')
                        lines.append('                                        ' + year + '\n')
                        lines.append('                                     </span>\n')
                        lines.append('                                  </div>\n')
                     if doi != "":
                        lines.append('                                  <div class="doi">\n')
                        lines.append('                                     <span>\n')
                        lines.append('                                        DOI:<a href=http://dx.doi.org/' + doi + '>' + doi + '<a>\n')
                        lines.append('                                     </span>\n')
                        lines.append('                                  </div>\n')
                     lines.append('                               </div>\n')
                     lines.append('                            </div>\n')
                     if abstract != "":
                        lines.append('                            <div class="item-abstract">\n')
                        lines.append('                               <span>\n')
                        lines.append('                                  ' + abstract + '\n')
                        lines.append('                               </span>\n')
                        lines.append('                            </div>\n')
                     if keywords != "":
                        lines.append('                            <div class="item-keywords">\n')
                        lines.append('                               <span>\n')
                        lines.append('                                  ' + keywords + '\n')
                        lines.append('                               </span>\n')
                        lines.append('                            </div>\n')
                     lines.append('                          </div>\n')
                     lines.append(line)
                  else:
                     lines.append(line)
                  
            with codecs.open(pathHTML,'w','utf-8') as fileHTML:
               for line in lines:
                  fileHTML.write(line)
            if (count//500)%2 > 0 and (count//50)%2 > 0:
               if randint(0,100) > 50:
                  time.sleep(randint(5,120))
               if randint(0,100) < 50:
                  randompage = mech.open(websites[randint(1,20)])
                  randomhtml = pagemain.read()
                  time.sleep(randint(5,120))
            
      
   with open(pathHTML,"a") as fileHTML:
      fileHTML.write("		</ol>\n")
      fileHTML.write("	</body>\n")
      fileHTML.write("</html>\n")
'''   
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"
   print "                           PUBLICATIONS"
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"
   for pub in pubs:
      print "----------------------------------------------------------------------"
      for info in pub:
         print info
      print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"   
'''

def scrape_elsevier(username, password, url, string):
   if username!='':
      # Browser
      mech = mechanize.Browser()
      
      # Enable cookie support for urllib2 
      cookiejar = cookielib.LWPCookieJar() 
      mech.set_cookiejar( cookiejar )
      
      # Broser options 
      mech.set_handle_equiv( True ) 
      mech.set_handle_gzip( True ) 
      mech.set_handle_redirect( True ) 
      mech.set_handle_referer( True ) 
      mech.set_handle_robots( False ) 
            
      mech.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 ) 
      mech.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'), ('Accept', '*/*')]
            
      authurl = "https://auth.univ-lorraine.fr/login;jsessionid=5FA92013464241CD2F055D8305BF77E1?service=http%3A%2F%2Fauth-bases-doc.univ-lorraine.fr%2Findex.php%3Furl%3Dhttp%253a%252f%252fwww.sciencedirect.com%252f%26logup%3Dfalse application/x-www-form-urlencoded"
            
      mech.open(authurl)
      mech.select_form(nr=0)
      mech[ "username" ] = username
      mech[ "password" ] = password
      res = mech.submit() 
            
      page = mech.open(url)
      mech.select_form(name="qkSrch")
      mech[ "qs_all" ] = string
      res = mech.submit() 
      html = res.read()
      with open("elsevier_search.html","w") as htmlfile:
         htmlfile.write(html)
   

def main(argv):
   database = ''
   searchstring = ''
   outputfile = ''
   baseurl = ''
   username = ''
   password = ''
   page = 0
   try:
      opts, args = getopt.getopt(argv,"hd:s:o:u:p:pa:",["help","Help","data","database","searchstring","search","ofile","outfile","outputfile","username","user","password","pwd","page","Page"])
   except getopt.GetoptError:
      print 'test.py -d <database> -s <search string> -o <output file> -u <username> -p <password>  -pa <page>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h", "--help","--Help"):
         print ''
         print ''
         print '*********************************************************************************'
         print '*                                                                               *'
         print '*               A tool for scientific literature analysis                       *'
         print '*                                                                               *'
         print '*                                 by                                            *'
         print '*                                                                               *'
         print '*                        Luca Di Stasio, 2016                                   *'
         print '*                                                                               *'
         print '*********************************************************************************'
         print ''
         print 'Program syntax:'
         print 'search.py -d <database> -s <search string> -o <output file> -u <username> -p <password> -pa <page>'
         print ''
         print 'Mandatory arguments:'
         print '-d <database> -s <search string>'
         print ''
         print 'Optional arguments:'
         print '-o <output file> -u <username> -p <password> -pa <page>'
         print ''
         print 'Available databases:'
         print 'Database                                             Command-line option'
         print '--------------------------------------------------------------------------'
         print 'ACM Digital Library                                  ACM'
         print 'De Gruyter                                           De Gruyter'
         print 'DOAJ Directory of Open Access Journals               DOAJ'
         print 'GreenFile                                            GreenFile'
         print 'IEEE Xplore Digital Library                          IEEE'
         print 'Oxford Journals                                      Oxford Journals'
         print 'ScienceDirect Freedom (Elsevier)                     Elsevier'
         print 'SpringerLink                                         Springer'
         print 'Taylor & Francis                                     Taylor & Francis'
         print 'Techniques de l Ingenieur                            Techniques'
         print 'Wiley Online Library                                 Wiley'
         print 'WoS Web of Science                                   WoS'
         print 'Mendeley                                             Mendeley'
         print 'arXiv                                                arXiv'
         print ''
         sys.exit()
      elif opt in ("-d", "--data","--database"):
         database = arg
      elif opt in ("-s", "--searchstring","--search"):
         searchstring = arg
      elif opt in ("-o", "--ofile","--outfile","--outputfile"):
         outputfile = arg
      elif opt in ("-u", "--username","--user"):
         username = arg
      elif opt in ("-p", "--password","--pwd"):
         password = arg
      elif opt in ("-pa", "--page","--Page"):
         page = int(arg)
         
   if database=="Elsevier":
       baseurl = "http://www.sciencedirect.com.bases-doc.univ-lorraine.fr/"
   elif database=="Springer":
       baseurl = "http://link.springer.com.bases-doc.univ-lorraine.fr/"
   elif database=="WoS":
       baseurl = "http://apps.webofknowledge.com.bases-doc.univ-lorraine.fr/"
   elif database=="ACM":
       baseurl = "http://dl.acm.org.bases-doc.univ-lorraine.fr/"
   elif database=="De Gruyter":
       baseurl = "http://www.degruyter.com.bases-doc.univ-lorraine.fr/"
   elif database=="DOAJ":
       baseurl = "https://doaj.org/"
   elif database=="GreenFile":
       baseurl = "http://web.b.ebscohost.com.bases-doc.univ-lorraine.fr/ehost/"
   elif database=="IEEE":
       baseurl = "http://ieeexplore.ieee.org.bases-doc.univ-lorraine.fr/search/"
   elif database=="Oxford Journals":
       baseurl = "http://services.oxfordjournals.org.bases-doc.univ-lorraine.fr/cgi/"
   elif database=="Taylor & Francis":
       baseurl = "http://www.tandfonline.com.bases-doc.univ-lorraine.fr/action/"
   elif database=="Techniques":
       baseurl = "http://www.techniques-ingenieur.fr.bases-doc.univ-lorraine.fr/"
   elif database=="Wiley":
       baseurl = "http://onlinelibrary.wiley.com.bases-doc.univ-lorraine.fr/"
   elif database=="Mendeley":
       baseurl = "https://www.mendeley.com/research-papers/search/?query="
   elif database=="arXiv":
       baseurl = "http://arxiv.org/find/all/"
   else:
       baseurl = "www.google.com"
   
   #scrape_elsevier(username, password, baseurl, string)
   scrape_mendeley(baseurl, searchstring, outputfile, page)

if __name__ == "__main__":
   main(sys.argv[1:])