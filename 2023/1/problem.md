



Day 1 - Advent of Code 2023



window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});


[Advent of Code](/)
===================

* [[About]](/2023/about)
* [[Events]](/2023/events)
* [[Shop]](https://teespring.com/stores/advent-of-code)
* [[Log In]](/2023/auth/login)
 {'year':[2023](/2023)}
=======================

* [[Calendar]](/2023)
* [[AoC++]](/2023/support)
* [[Sponsors]](/2023/sponsors)
* [[Leaderboard]](/2023/leaderboard)
* [[Stats]](/2023/stats)


Our [sponsors](/2023/sponsors) help make Advent of Code possible:[Smarty](https://www.smarty.com/advent-of-code) - Join our private leaderboard and solve our puzzles for BIG PRIZES!!! ----------------- Address Validation and Autocomplete, and more!


--- Day 1: Trebuchet?! ---
--------------------------

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.


You've been doing this long enough to know that to restore snow operations, you need to check all *fifty stars* by December 25th.


Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants *one star*. Good luck!


You try to ask why they can't just use a [weather machine](/2015/day/1) ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a [trebuchet](https://en.wikipedia.org/wiki/Trebuchet) ("please hold still, we need to strap you in").


As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been *amended* by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.


The newly-improved calibration document consists of lines of text; each line originally contained a specific *calibration value* that the Elves now need to recover. On each line, the calibration value can be found by combining the *first digit* and the *last digit* (in that order) to form a single *two-digit number*.


For example:



```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

```

In this example, the calibration values of these four lines are `12`, `38`, `15`, and `77`. Adding these together produces `*142*`.


Consider your entire calibration document. *What is the sum of all of the calibration values?*



To play, please identify yourself via one of these services:


[[GitHub]](/auth/github) [[Google]](/auth/google) [[Twitter]](/auth/twitter) [[Reddit]](/auth/reddit) - [[How Does Auth Work?]](/about#faq_auth)





(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1\*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-69522494-1', 'auto');
ga('set', 'anonymizeIp', true);
ga('send', 'pageview');



