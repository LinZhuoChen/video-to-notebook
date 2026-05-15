---
course_slug: diffusion-principles-vizuara
idx: 9
title: Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of
  Diffusion Models
video_url: https://www.youtube.com/watch?v=Yyir7-OAnlA
duration_sec: null
chunks:
- idx: 0
  start_sec: 5.51
  end_sec: 77.91
  text: 'Hello everyone and welcome to the second Hello everyone and welcome to the
    second

    lecture of the course principles of lecture of the course principles of lecture
    of the course principles of

    diffusion models. diffusion models. diffusion models.

    Today I''m going to cover a very Today I''m going to cover a very Today I''m going
    to cover a very

    interesting topic interesting topic interesting topic

    which has been on my mind since a very which has been on my mind since a very
    which has been on my mind since a very

    long time and u today is when I''ll be long time and u today is when I''ll be
    long time and u today is when I''ll be

    teaching you about this topic from teaching you about this topic from teaching
    you about this topic from

    scratch. scratch. scratch.

    The name of the topic which we are going The name of the topic which we are going
    The name of the topic which we are going

    to learn today is called as variational to learn today is called as variational
    to learn today is called as variational

    autoenccoders. autoenccoders. autoenccoders.

    You might see this name popping up in a You might see this name popping up in
    a You might see this name popping up in a

    lot of research papers. lot of research papers. lot of research papers.

    This term is now commonly used in This term is now commonly used in This term
    is now commonly used in

    multiple research papers involving large multiple research papers involving large
    multiple research papers involving large

    language models. language models. language models.

    However, understanding variation However, understanding variation However, understanding
    variation

    autoenccoders is not very autoenccoders is not very autoenccoders is not very

    straightforward straightforward straightforward

    and a lot of people just blindly use and a lot of people just blindly use and
    a lot of people just blindly use

    this term without fully acknowledging this term without fully acknowledging this
    term without fully acknowledging

    the the the

    meaning of the conceptual framework meaning of the conceptual framework meaning
    of the conceptual framework

    which forms the foundation behind which forms the foundation behind which forms
    the foundation behind

    variation autoenccoders or VAEs. variation autoenccoders or VAEs. variation autoenccoders
    or VAEs.

    So we are going to understand everything So we are going to understand everything
    So we are going to understand everything

    from scratch.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 1
  start_sec: 77.91
  end_sec: 139.83
  text: 'from scratch. from scratch.

    And this lecture is And this lecture is And this lecture is

    going to be very important for the going to be very important for the going to
    be very important for the

    subsequent lectures where we''ll start subsequent lectures where we''ll start
    subsequent lectures where we''ll start

    focusing on diffusion models. You will focusing on diffusion models. You will
    focusing on diffusion models. You will

    see that everything neatly builds upon see that everything neatly builds upon
    see that everything neatly builds upon

    what has come before. what has come before. what has come before.

    So uh I was recently listening to a So uh I was recently listening to a So uh
    I was recently listening to a

    podcast from Andri Arbati and uh he uses podcast from Andri Arbati and uh he uses
    podcast from Andri Arbati and uh he uses

    a very nice phrase where he says that a very nice phrase where he says that a
    very nice phrase where he says that

    whenever you learn something from whenever you learn something from whenever you
    learn something from

    scratch right you understand the gaps in scratch right you understand the gaps
    in scratch right you understand the gaps in

    your knowledge and this is exactly what your knowledge and this is exactly what
    your knowledge and this is exactly what

    we''ll be doing in this lecture. we''ll be doing in this lecture. we''ll be doing
    in this lecture.

    So what I''ll be doing is that I''ll be So what I''ll be doing is that I''ll be
    So what I''ll be doing is that I''ll be

    there is a tangle of information about there is a tangle of information about
    there is a tangle of information about

    VAS on the internet. So my focus will be VAS on the internet. So my focus will
    be VAS on the internet. So my focus will be

    to untangle this information and create to untangle this information and create
    to untangle this information and create

    a ramp for you so that you go from 0 to a ramp for you so that you go from 0 to
    a ramp for you so that you go from 0 to

    one. one. one.

    So let''s let''s start with the So let''s let''s start with the So let''s let''s
    start with the

    with the understanding of VAS.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 2
  start_sec: 139.83
  end_sec: 199.84
  text: 'with the understanding of VAS. with the understanding of VAS.

    So first we''ll take a simple example. So first we''ll take a simple example.
    So first we''ll take a simple example.

    Imagine that you have collected Imagine that you have collected Imagine that you
    have collected

    handwriting samples handwriting samples handwriting samples

    from all the students in your class. from all the students in your class. from
    all the students in your class.

    Let us say that these students have Let us say that these students have Let us
    say that these students have

    written the word hello. We are going to written the word hello. We are going to
    written the word hello. We are going to

    assume that there are 100 students assume that there are 100 students assume that
    there are 100 students

    sitting in the classroom and all of them sitting in the classroom and all of them
    sitting in the classroom and all of them

    have written the word hello on a sheet have written the word hello on a sheet
    have written the word hello on a sheet

    of paper. of paper. of paper.

    So just imagine this process happening So just imagine this process happening
    So just imagine this process happening

    in your mind. Students will write the in your mind. Students will write the in
    your mind. Students will write the

    word hello in many different ways. Some word hello in many different ways. Some
    word hello in many different ways. Some

    of us have handwriting which is slanted of us have handwriting which is slanted
    of us have handwriting which is slanted

    a bit towards left. Some of us will a bit towards left. Some of us will a bit
    towards left. Some of us will

    write words which are slanted a bit write words which are slanted a bit write
    words which are slanted a bit

    towards right. Some of us have a very towards right. Some of us have a very towards
    right. Some of us have a very

    neat handwriting. Some of us have messy neat handwriting. Some of us have messy
    neat handwriting. Some of us have messy

    [snorts] handwriting. Some of us write [snorts] handwriting. Some of us write
    [snorts] handwriting. Some of us write

    in cursive. Some of us in cursive. Some of us'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 3
  start_sec: 199.84
  end_sec: 266.88
  text: 'in cursive. Some of us

    u don''t write in cursive. So there are a u don''t write in cursive. So there
    are a u don''t write in cursive. So there are a

    lot of different ways in which people lot of different ways in which people lot
    of different ways in which people

    can or students in your class can write can or students in your class can write
    can or students in your class can write

    this word hello. this word hello. this word hello.

    Now once Now once Now once

    you have imagined this in your mind let you have imagined this in your mind let
    you have imagined this in your mind let

    me come to the main premise of today''s me come to the main premise of today''s
    me come to the main premise of today''s

    lecture. So let us say that someone lecture. So let us say that someone lecture.
    So let us say that someone

    comes to you and ask comes to you and ask comes to you and ask

    and asks that okay fine and asks that okay fine and asks that okay fine

    give me a machine which can produce give me a machine which can produce give me
    a machine which can produce

    samples of handwriting of the word hello samples of handwriting of the word hello
    samples of handwriting of the word hello

    which will match the styles which will match the styles which will match the styles

    of of of

    the handwriting the handwriting the handwriting

    written by the students of your class. written by the students of your class.
    written by the students of your class.

    So imagine a machine where you press a So imagine a machine where you press a
    So imagine a machine where you press a

    button. You get a sheet of paper. You button. You get a sheet of paper. You button.
    You get a sheet of paper. You

    get hello written on it. And this hello get hello written on it. And this hello
    get hello written on it. And this hello

    should match the style of someone in should match the style of someone in should
    match the style of someone in

    your class. your class. your class.

    Then another time you press a button. Then another time you press a button.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 4
  start_sec: 266.88
  end_sec: 335.12
  text: 'Then another time you press a button.

    Another time you get another hello. This Another time you get another hello. This
    Another time you get another hello. This

    time it might be some different student time it might be some different student
    time it might be some different student

    but it is still from the samples but it is still from the samples but it is still
    from the samples

    collected from the students of your collected from the students of your collected
    from the students of your

    class only. class only. class only.

    How will you generate such a machine? How will you generate such a machine? How
    will you generate such a machine?

    This might take you back to uh some This might take you back to uh some This might
    take you back to uh some

    classic magic movies like the prestige classic magic movies like the prestige
    classic magic movies like the prestige

    for example where [snorts] there are for example where [snorts] there are for
    example where [snorts] there are

    these antique machines which produce these antique machines which produce these
    antique machines which produce

    something. there is some something. there is some something. there is some

    mechanical uh wizardry which goes on mechanical uh wizardry which goes on mechanical
    uh wizardry which goes on

    inside the machine and finally you get inside the machine and finally you get
    inside the machine and finally you get

    something out of it. something out of it. something out of it.

    But uh let us think from scratch how how But uh let us think from scratch how
    how But uh let us think from scratch how how

    do we generate a machine which can do we generate a machine which can do we generate
    a machine which can

    produce samples of handwriting of this produce samples of handwriting of this
    produce samples of handwriting of this

    word hello word hello word hello

    in a more theoretical in a more theoretical in a more theoretical

    description. What we want to do is that description. What we want to do is that
    description. What we want to do is that

    we want to we want to we want to

    generate a sample generate a sample generate a sample

    such that or generate a machine such such that or generate a machine such'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 5
  start_sec: 335.12
  end_sec: 405.51
  text: 'such that or generate a machine such

    that the samples drawn from that machine that the samples drawn from that machine
    that the samples drawn from that machine

    are from the probability distribution are from the probability distribution are
    from the probability distribution

    of the handwriting samples of the of the handwriting samples of the of the handwriting
    samples of the

    students of your class. students of your class. students of your class.

    So So So

    we can reframe this question as we want we can reframe this question as we want
    we can reframe this question as we want

    to predict the probability distribution to predict the probability distribution
    to predict the probability distribution

    of the handwriting of the students of of the handwriting of the students of of
    the handwriting of the students of

    your class your class your class

    which is very closely tied with what we which is very closely tied with what we
    which is very closely tied with what we

    discussed in the first lecture which is discussed in the first lecture which is
    discussed in the first lecture which is

    deep generative modeling. This is one of deep generative modeling. This is one
    of deep generative modeling. This is one of

    the main objectives of deep generative the main objectives of deep generative
    the main objectives of deep generative

    modeling. Okay. Now the question is how will you Okay. Now the question is how
    will you

    solve this problem? solve this problem? solve this problem?

    The the first thing that will come to The the first thing that will come to The
    the first thing that will come to

    your mind is that your mind is that your mind is that

    okay so first of all I need to okay so first of all I need to okay so first of
    all I need to

    understand how is this handwriting understand how is this handwriting understand
    how is this handwriting

    generated in in the first place. generated in in the first place. generated in
    in the first place.

    So the the first thought that might come So the the first thought that might come
    So the the first thought that might come

    to your mind is what are the hidden to your mind is what are the hidden to your
    mind is what are the hidden

    factors that determine the style of the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 6
  start_sec: 405.51
  end_sec: 483.99
  text: 'factors that determine the style of the factors that determine the style
    of the

    handwriting. handwriting. handwriting.

    So each student handwriting depends on So each student handwriting depends on
    So each student handwriting depends on

    many hidden characteristics. For many hidden characteristics. For many hidden
    characteristics. For

    example, how much pressure they apply, example, how much pressure they apply,
    example, how much pressure they apply,

    whether they write slanted, whether whether they write slanted, whether whether
    they write slanted, whether

    their letters are wide or their letters their letters are wide or their letters
    their letters are wide or their letters

    are narrow, how fast they write, how are narrow, how fast they write, how are
    narrow, how fast they write, how

    neat they write, etc. So there are a lot neat they write, etc. So there are a
    lot neat they write, etc. So there are a lot

    of hidden characteristics of hidden characteristics of hidden characteristics

    which affect the handwriting of a which affect the handwriting of a which affect
    the handwriting of a

    student. student. student.

    And you might think that okay fine so And you might think that okay fine so And
    you might think that okay fine so

    what if I capture all these what if I capture all these what if I capture all
    these

    characteristics and characteristics and characteristics and

    write some function which takes these write some function which takes these write
    some function which takes these

    characteristics as an input and then characteristics as an input and then characteristics
    as an input and then

    produces the handwriting as the output. produces the handwriting as the output.
    produces the handwriting as the output.

    So uh this is this is the line of So uh this is this is the line of So uh this
    is this is the line of

    thinking which thinking which thinking which

    is the most intuitive in the beginning. is the most intuitive in the beginning.
    is the most intuitive in the beginning.

    Now these characteristics are not seen Now these characteristics are not seen
    Now these characteristics are not seen

    in the final image in the final image in the final image

    but they definitely influence the shape but they definitely influence the shape
    but they definitely influence the shape

    of the letters. of the letters. of the letters.

    So my first intuition is that okay fine'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 7
  start_sec: 483.99
  end_sec: 542.63
  text: 'So my first intuition is that okay fine So my first intuition is that okay
    fine

    my first job is to figure out all these my first job is to figure out all these
    my first job is to figure out all these

    hidden characteristics hidden characteristics hidden characteristics

    and then what I will do is I will create and then what I will do is I will create
    and then what I will do is I will create

    a mapping from these hidden a mapping from these hidden a mapping from these hidden

    characteristics to the handwriting characteristics to the handwriting characteristics
    to the handwriting

    samples. samples. samples.

    Once I do that once the mapping is Once I do that once the mapping is Once I do
    that once the mapping is

    already created all I need is to feed an already created all I need is to feed
    an already created all I need is to feed an

    input into my machine. And since the input into my machine. And since the input
    into my machine. And since the

    mapping is already created, I can create mapping is already created, I can create
    mapping is already created, I can create

    the the

    output which is output which is output which is

    related to the input based on my related to the input based on my related to the
    input based on my

    mapping. mapping. mapping.

    So this is how I''m I''m thinking of this So this is how I''m I''m thinking of
    this So this is how I''m I''m thinking of this

    problem for from from first principles. problem for from from first principles.
    problem for from from first principles.

    Now uh we can rethink our thoughts in a Now uh we can rethink our thoughts in
    a Now uh we can rethink our thoughts in a

    way that we can say that okay these are way that we can say that okay these are
    way that we can say that okay these are

    the hidden factors which influence the the hidden factors which influence the
    the hidden factors which influence the

    handwriting which can also be called as handwriting which can also be called as
    handwriting which can also be called as

    a secret recipe that determines the a secret recipe that determines the a secret
    recipe that determines the

    final shape of the handwriting.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 8
  start_sec: 542.63
  end_sec: 597.11
  text: 'final shape of the handwriting. final shape of the handwriting.

    So once you capture the secret recipe So once you capture the secret recipe So
    once you capture the secret recipe

    for for for

    a student you can determine their a student you can determine their a student
    you can determine their

    handwriting. So you can assume that handwriting. So you can assume that handwriting.
    So you can assume that

    there is a 1:1 mapping from the secret there is a 1:1 mapping from the secret
    there is a 1:1 mapping from the secret

    recipe to the handwriting. recipe to the handwriting. recipe to the handwriting.

    For example, if the secret recipe is if For example, if the secret recipe is if
    For example, if the secret recipe is if

    your friend writes slightly tilted, thin your friend writes slightly tilted, thin
    your friend writes slightly tilted, thin

    strokes, medium speed, moderate strokes, medium speed, moderate strokes, medium
    speed, moderate

    neatness, neatness, neatness,

    you can generate the handwriting hello. you can generate the handwriting hello.
    you can generate the handwriting hello.

    This is a rough assumption. There might This is a rough assumption. There might
    This is a rough assumption. There might

    be a lot of other factors which be a lot of other factors which be a lot of other
    factors which

    determine some of which we we would not determine some of which we we would not
    determine some of which we we would not

    be even able to guess what these hidden be even able to guess what these hidden
    be even able to guess what these hidden

    factors are. But this is what our brain factors are. But this is what our brain
    factors are. But this is what our brain

    tells us initially. There might be tells us initially. There might be tells us
    initially. There might be

    hundreds of factors but uh we have come hundreds of factors but uh we have come
    hundreds of factors but uh we have come

    up with five factors which are mentioned up with five factors which are mentioned
    up with five factors which are mentioned

    in these bullet points over here. in these bullet points over here. in these bullet
    points over here.

    So the general architecture of the So the general architecture of the So the general
    architecture of the

    machine looks as follows.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 9
  start_sec: 597.11
  end_sec: 652.8
  text: 'machine looks as follows. machine looks as follows.

    Secret recipe is given as an input to Secret recipe is given as an input to Secret
    recipe is given as an input to

    the machine. The machine takes this the machine. The machine takes this the machine.
    The machine takes this

    secret recipe and the machine produces secret recipe and the machine produces
    secret recipe and the machine produces

    an output which is a handwriting style. an output which is a handwriting style.
    an output which is a handwriting style.

    So you feed a different secret recipe, So you feed a different secret recipe,
    So you feed a different secret recipe,

    you get a different handwriting style. you get a different handwriting style.
    you get a different handwriting style.

    [snorts] [snorts] [snorts]

    So imagine So imagine So imagine

    a hardware in front of you, an antique a hardware in front of you, an antique
    a hardware in front of you, an antique

    hardware where you have six knobs for hardware where you have six knobs for hardware
    where you have six knobs for

    the secret recipe. And for each knob you the secret recipe. And for each knob
    you the secret recipe. And for each knob you

    have three different buttons. have three different buttons. have three different
    buttons.

    So let''s say how much pressure you So let''s say how much pressure you So let''s
    say how much pressure you

    apply. There are three buttons, low, apply. There are three buttons, low, apply.
    There are three buttons, low,

    medium, high. whether they are slanted, medium, high. whether they are slanted,
    medium, high. whether they are slanted,

    left, right, center. You press six left, right, center. You press six left, right,
    center. You press six

    buttons and at the end of it you get a buttons and at the end of it you get a
    buttons and at the end of it you get a

    printed sheet of paper which gives you printed sheet of paper which gives you
    printed sheet of paper which gives you

    the handwriting for that specific the handwriting for that specific the handwriting
    for that specific

    recipe. recipe. recipe.

    So this looks uh So this looks uh So this looks uh

    interesting, right? It it it looks like interesting, right? It it it looks like'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 10
  start_sec: 652.8
  end_sec: 713.43
  text: 'interesting, right? It it it looks like

    okay fine this this it it makes a lot of okay fine this this it it makes a lot
    of okay fine this this it it makes a lot of

    sense. [snorts] sense. [snorts] sense. [snorts]

    Now in uh in in literature the secret Now in uh in in literature the secret Now
    in uh in in literature the secret

    recipe is something which is called as a recipe is something which is called as
    a recipe is something which is called as a

    latent variable. latent variable. latent variable.

    Why latent? Because these are hidden Why latent? Because these are hidden Why
    latent? Because these are hidden

    factors which determine the handwriting factors which determine the handwriting
    factors which determine the handwriting

    style. style. style.

    Uh and these variables are denoted by Uh and these variables are denoted by Uh
    and these variables are denoted by

    the symbol zed or z. The latent variable the symbol zed or z. The latent variable
    the symbol zed or z. The latent variable

    zed capture the essence of how the zed capture the essence of how the zed capture
    the essence of how the

    handwriting was formed. handwriting was formed. handwriting was formed.

    U as we saw here there are 1 2 3 4 five U as we saw here there are 1 2 3 4 five
    U as we saw here there are 1 2 3 4 five

    Latin variables which capture the Latin variables which capture the Latin variables
    which capture the

    essence of the handwriting or the secret essence of the handwriting or the secret
    essence of the handwriting or the secret

    recipe behind the handwriting and these recipe behind the handwriting and these
    recipe behind the handwriting and these

    factors are hidden you you don''t know factors are hidden you you don''t know
    factors are hidden you you don''t know

    what these factors are when you see the what these factors are when you see the
    what these factors are when you see the

    handwriting of a student right that''s handwriting of a student right that''s
    handwriting of a student right that''s

    why they are called as latent or hidden why they are called as latent or hidden
    why they are called as latent or hidden

    variables variables variables

    now um in the rest of this lecture we We'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 11
  start_sec: 713.43
  end_sec: 774.639
  text: 'now um in the rest of this lecture we We now um in the rest of this lecture
    we We

    are going to assume that are going to assume that are going to assume that

    for the handwriting example that we took for the handwriting example that we took
    for the handwriting example that we took

    there are only two latent variables of there are only two latent variables of
    there are only two latent variables of

    interest. interest. interest.

    One which captures the slantness of the One which captures the slantness of the
    One which captures the slantness of the

    handwriting and one which captures the handwriting and one which captures the
    handwriting and one which captures the

    neatness of the handwriting. So we are neatness of the handwriting. So we are
    neatness of the handwriting. So we are

    going to assume that once we know the going to assume that once we know the going
    to assume that once we know the

    slantness and the neatness slantness and the neatness slantness and the neatness

    we can determine the handwriting of a we can determine the handwriting of a we
    can determine the handwriting of a

    student. student.

    [snorts] So in literature you might see [snorts] So in literature you might see
    [snorts] So in literature you might see

    these words latin variables these words latin variables these words latin variables

    written written written

    um and um and um and

    I don''t want you to get bothered by that I don''t want you to get bothered by
    that I don''t want you to get bothered by that

    because it simply means that there are because it simply means that there are
    because it simply means that there are

    some underlying factors behind some underlying factors behind some underlying
    factors behind

    a distribution which we don''t know a distribution which we don''t know a distribution
    which we don''t know

    about. about. about.

    For example, here I have assumed that For example, here I have assumed that For
    example, here I have assumed that

    there are two underlying factors. there are two underlying factors. there are
    two underlying factors.

    uh but in a real life problem we will uh but in a real life problem we will uh
    but in a real life problem we will

    not know these factors beforehand. That not know these factors beforehand. That'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 12
  start_sec: 774.639
  end_sec: 831.839
  text: 'not know these factors beforehand. That

    is why they are called as latent is why they are called as latent is why they
    are called as latent

    variables. variables. variables.

    So So

    intuitively we think that we are going intuitively we think that we are going
    intuitively we think that we are going

    one level deeper to generate something one level deeper to generate something
    one level deeper to generate something

    at a surface level. So it''s like you at a surface level. So it''s like you at
    a surface level. So it''s like you

    want to generate the handwriting but to want to generate the handwriting but to
    want to generate the handwriting but to

    generate the handwriting you first need generate the handwriting you first need
    generate the handwriting you first need

    to understand what is the factors to understand what is the factors to understand
    what is the factors

    influencing the handwriting and then you influencing the handwriting and then
    you influencing the handwriting and then you

    go up and then you generate the go up and then you generate the go up and then
    you generate the

    handwriting. handwriting.

    So it''s like a swimmer who is going deep So it''s like a swimmer who is going
    deep So it''s like a swimmer who is going deep

    into the ocean and then coming up to the into the ocean and then coming up to
    the into the ocean and then coming up to the

    surface. So we are essentially probing surface. So we are essentially probing
    surface. So we are essentially probing

    the depth of u the the factors which are the depth of u the the factors which
    are the depth of u the the factors which are

    influencing the distribution. influencing the distribution. influencing the distribution.

    Okay. So uh we can represent this in in Okay. So uh we can represent this in in
    Okay. So uh we can represent this in in

    the form of a graph a 2D graph. The the form of a graph a 2D graph. The the form
    of a graph a 2D graph. The

    x-axis x-axis x-axis

    is represented by the symbol z1 and the is represented by the symbol z1 and the
    is represented by the symbol z1 and the

    y-axis is represented by the symbol zed y-axis is represented by the symbol zed'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 13
  start_sec: 831.839
  end_sec: 888.16
  text: 'y-axis is represented by the symbol zed

    2. Zed1 stands for slantness of the 2. Zed1 stands for slantness of the 2. Zed1
    stands for slantness of the

    handwriting and zed2 stands for neatness handwriting and zed2 stands for neatness
    handwriting and zed2 stands for neatness

    of the handwriting. of the handwriting. of the handwriting.

    What do I mean by slantness? What do I mean by slantness? What do I mean by slantness?

    This is This is This is

    slanted towards the left. This is slanted towards the left. This is slanted towards
    the left. This is

    slanted towards the right etc. slanted towards the right etc. slanted towards
    the right etc.

    And neatness is uh obvious. Neatness is And neatness is uh obvious. Neatness is
    And neatness is uh obvious. Neatness is

    whether your handwriting is neat or whether your handwriting is neat or whether
    your handwriting is neat or

    messy. messy. messy.

    So just some examples here. You can see So just some examples here. You can see
    So just some examples here. You can see

    that on the right uh on the right hand that on the right uh on the right hand
    that on the right uh on the right hand

    side here you have words which are side here you have words which are side here
    you have words which are

    slanted towards the right and on the slanted towards the right and on the slanted
    towards the right and on the

    left hand side you have words which are left hand side you have words which are
    left hand side you have words which are

    slanted towards the left and slanted towards the left and slanted towards the
    left and

    you go above or below the axis you have you go above or below the axis you have
    you go above or below the axis you have

    words which are not very neat. So the words which are not very neat. So the words
    which are not very neat. So the

    central point is indicating that the central point is indicating that the central
    point is indicating that the

    words are neat. But if you go above or words are neat. But if you go above or
    words are neat. But if you go above or

    below it''s it''s not neat. below it''s it''s not neat.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 14
  start_sec: 888.16
  end_sec: 933.269
  text: 'below it''s it''s not neat.

    So I have made some spelling mistake So I have made some spelling mistake So I
    have made some spelling mistake

    here. But what I want to show is I want here. But what I want to show is I want
    here. But what I want to show is I want

    to show words which are written in a to show words which are written in a to show
    words which are written in a

    very messy way. Something like this. very messy way. Something like this. very
    messy way. Something like this.

    Yeah, this is like really messy. So I Yeah, this is like really messy. So I Yeah,
    this is like really messy. So I

    hope you get the point. hope you get the point. hope you get the point.

    Um okay. Okay. So from the above graph Um okay. Okay. So from the above graph
    Um okay. Okay. So from the above graph

    you can see that both the axis carry you can see that both the axis carry you
    can see that both the axis carry

    some meaning. Words which are on the some meaning. Words which are on the some
    meaning. Words which are on the

    right hand side are more slanted towards right hand side are more slanted towards
    right hand side are more slanted towards

    the right and words which are on the the right and words which are on the the
    right and words which are on the

    left hand side are more slanted towards left hand side are more slanted towards
    left hand side are more slanted towards

    the left and words which are on the top the left and words which are on the top
    the left and words which are on the top

    or down are very very messy. or down are very very messy. or down are very very
    messy.

    Now we can see that every single point Now we can see that every single point
    Now we can see that every single point

    on this plane corresponds to a specific on this plane corresponds to a specific
    on this plane corresponds to a specific

    style of handwriting. So this is the style of handwriting. So this is the style
    of handwriting. So this is the

    mapping which I was talking about. For'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 15
  start_sec: 933.269
  end_sec: 991.91
  text: 'mapping which I was talking about. For mapping which I was talking about.
    For

    example, if you pick a point here, you example, if you pick a point here, you
    example, if you pick a point here, you

    know how slant it is, how neat it is, know how slant it is, how neat it is, know
    how slant it is, how neat it is,

    and then you can generate a handwriting and then you can generate a handwriting
    and then you can generate a handwriting

    for for that point. [snorts] for for that point. [snorts] for for that point.
    [snorts]

    How to generate this handwriting is How to generate this handwriting is How to
    generate this handwriting is

    something we will discuss. But for now, something we will discuss. But for now,
    something we will discuss. But for now,

    all you need to know is that there is a all you need to know is that there is
    a all you need to know is that there is a

    mapping which we are creating between mapping which we are creating between mapping
    which we are creating between

    the Latin space the Latin space the Latin space

    and the true distribution. So for example for all the 100 students So for example
    for all the 100 students

    in your class the distribution might in your class the distribution might in your
    class the distribution might

    look like follows. So you might be look like follows. So you might be look like
    follows. So you might be

    somewhere here. Your friend might be somewhere here. Your friend might be somewhere
    here. Your friend might be

    neat but slanted towards the neat but slanted towards the neat but slanted towards
    the

    left. Some of your friends who whose left. Some of your friends who whose left.
    Some of your friends who whose

    handwriting is very bad and who are very handwriting is very bad and who are very
    handwriting is very bad and who are very

    slant either might be here or here etc. slant either might be here or here etc.
    slant either might be here or here etc.

    [snorts] So there are 100 samples here [snorts] So there are 100 samples here
    [snorts] So there are 100 samples here

    which correspond to every single student which correspond to every single student
    which correspond to every single student

    in your class.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 16
  start_sec: 991.91
  end_sec: 1057.27
  text: 'in your class. in your class.

    So this is also called as the So this is also called as the So this is also called
    as the

    distribution in the latent space of the distribution in the latent space of the
    distribution in the latent space of the

    handwriting styles. handwriting styles. handwriting styles.

    So So

    in in in future lectures and even in in in in future lectures and even in in in
    in future lectures and even in

    this lecture we are going to use the this lecture we are going to use the this
    lecture we are going to use the

    Latin space definition for other Latin space definition for other Latin space
    definition for other

    examples also. So examples also. So examples also. So

    the definition and the meaning of Latin the definition and the meaning of Latin
    the definition and the meaning of Latin

    space is generalizable for other use space is generalizable for other use space
    is generalizable for other use

    cases as well. cases as well. cases as well.

    Now we observe that each handwriting Now we observe that each handwriting Now
    we observe that each handwriting

    image is compressed in just two numbers image is compressed in just two numbers
    image is compressed in just two numbers

    slant and neatness. slant and neatness. slant and neatness.

    So you will see this very commonly that So you will see this very commonly that
    So you will see this very commonly that

    Latin space is typically Latin space is typically Latin space is typically

    of lower dimensions compared to the of lower dimensions compared to the of lower
    dimensions compared to the

    actual data distribution or we can say actual data distribution or we can say
    actual data distribution or we can say

    that the latin space is compressed that the latin space is compressed that the
    latin space is compressed

    compared to the real data distribution. compared to the real data distribution.
    compared to the real data distribution.

    So there is a huge amount of compression So there is a huge amount of compression
    So there is a huge amount of compression

    going here. You can see that we have going here. You can see that we have going
    here. You can see that we have

    compressed everything from a so a compressed everything from a so a compressed
    everything from a so a

    typical handwriting'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 17
  start_sec: 1057.27
  end_sec: 1119.19
  text: 'typical handwriting typical handwriting

    let''s say it is divided into 28x 28 let''s say it is divided into 28x 28 let''s
    say it is divided into 28x 28

    pixels. pixels. pixels.

    So there are 784 numbers right which so So there are 784 numbers right which so
    So there are 784 numbers right which so

    I''m writing hello here. Now we have I''m writing hello here. Now we have I''m
    writing hello here. Now we have

    compressed from 788 to 2 which is a huge compressed from 788 to 2 which is a huge
    compressed from 788 to 2 which is a huge

    amount of compression. amount of compression. amount of compression.

    um and similar handwritings end up as um and similar handwritings end up as um
    and similar handwritings end up as

    nearby points in this 2D latin space. nearby points in this 2D latin space. nearby
    points in this 2D latin space.

    Okay. So just one quick Okay. So just one quick Okay. So just one quick

    digression because we are going to digression because we are going to digression
    because we are going to

    discuss that eventually a bit later. So discuss that eventually a bit later. So
    discuss that eventually a bit later. So

    right now you you will see that there is right now you you will see that there
    is right now you you will see that there is

    a distribution of these handwriting a distribution of these handwriting a distribution
    of these handwriting

    styles which is centered around the mean styles which is centered around the mean
    styles which is centered around the mean

    which is centered around zero. It almost which is centered around zero. It almost
    which is centered around zero. It almost

    appears like everything is coming within appears like everything is coming within
    appears like everything is coming within

    a circle. Right? a circle. Right? a circle. Right?

    So this is called as a uniform or or a So this is called as a uniform or or a
    So this is called as a uniform or or a

    gshian distribution where all the gshian distribution where all the gshian distribution
    where all the

    samples or the distribution of in in the samples or the distribution of in in
    the samples or the distribution of in in the

    latent space is has a mean of zero and a'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 18
  start_sec: 1119.19
  end_sec: 1167.12
  text: 'latent space is has a mean of zero and a latent space is has a mean of zero
    and a

    standard deviation of one or any other standard deviation of one or any other
    standard deviation of one or any other

    value. But it in in 1D the gshian looks value. But it in in 1D the gshian looks
    value. But it in in 1D the gshian looks

    like this like this like this

    where if you take just zed 1 you will where if you take just zed 1 you will where
    if you take just zed 1 you will

    see a distribution like this. If you see a distribution like this. If you see
    a distribution like this. If you

    take zed 2 you will see a distribution take zed 2 you will see a distribution
    take zed 2 you will see a distribution

    like this centered around the mean which like this centered around the mean which
    like this centered around the mean which

    is zero for both in this case. And the is zero for both in this case. And the
    is zero for both in this case. And the

    deviation also looks so the deviation deviation also looks so the deviation deviation
    also looks so the deviation

    for zed 1 looks to be around one and the for zed 1 looks to be around one and
    the for zed 1 looks to be around one and the

    deviation for zed 2 also is around one. deviation for zed 2 also is around one.
    deviation for zed 2 also is around one.

    So u this is a bit mathematical. So even So u this is a bit mathematical. So even
    So u this is a bit mathematical. So even

    if you don''t completely understand this if you don''t completely understand this
    if you don''t completely understand this

    it is fine. I just want you to keep this it is fine. I just want you to keep this
    it is fine. I just want you to keep this

    in your mind as as we move ahead. Okay. in your mind as as we move ahead. Okay.
    in your mind as as we move ahead. Okay.

    So for now what we have seen is that we So for now what we have seen is that we'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 19
  start_sec: 1167.12
  end_sec: 1234.72
  text: 'So for now what we have seen is that we

    have this general architecture for the have this general architecture for the
    have this general architecture for the

    machine which takes the secret recipe as machine which takes the secret recipe
    as machine which takes the secret recipe as

    the input and then it produces the the input and then it produces the the input
    and then it produces the

    handwriting as the output. Okay. So, uh Okay. So, uh

    now now now

    this so so the input the secret recipe this so so the input the secret recipe
    this so so the input the secret recipe

    can also be written as a distribution in can also be written as a distribution
    in can also be written as a distribution in

    the latin space. the latin space. the latin space.

    So initially I had written secret recipe So initially I had written secret recipe
    So initially I had written secret recipe

    over here. But now I have replaced that over here. But now I have replaced that
    over here. But now I have replaced that

    by this distribution in the Latin space by this distribution in the Latin space
    by this distribution in the Latin space

    where every dot corresponds to a where every dot corresponds to a where every
    dot corresponds to a

    handwriting of a student. handwriting of a student. handwriting of a student.

    So the secret recipe should capture the So the secret recipe should capture the
    So the secret recipe should capture the

    hidden characteristics of my students hidden characteristics of my students hidden
    characteristics of my students

    and this is exactly what is being done and this is exactly what is being done
    and this is exactly what is being done

    in this Latin space distribution. in this Latin space distribution. in this Latin
    space distribution.

    So I give this as an input to the So I give this as an input to the So I give
    this as an input to the

    machine and I produce the output. machine and I produce the output. machine and
    I produce the output.

    Now the question is so so there is Now the question is so so there is Now the
    question is so so there is

    another word for this machine which is another word for this machine which is'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 20
  start_sec: 1234.72
  end_sec: 1304.72
  text: 'another word for this machine which is

    called as decoder. called as decoder. called as decoder.

    Let us quickly summarize what all we Let us quickly summarize what all we Let
    us quickly summarize what all we

    have learned till now in a beautiful have learned till now in a beautiful have
    learned till now in a beautiful

    animation which can which will show you animation which can which will show you
    animation which can which will show you

    how the decoder works for this same how the decoder works for this same how the
    decoder works for this same

    example of handwriting samples so that example of handwriting samples so that
    example of handwriting samples so that

    it becomes clear to everyone. [snorts]

    So we are converting from Latin style So we are converting from Latin style So
    we are converting from Latin style

    zed to handwriting X. The Latin space zed to handwriting X. The Latin space zed
    to handwriting X. The Latin space

    has two dimensions. has two dimensions. has two dimensions.

    uh we have variable zed 1 and zed2 which uh we have variable zed 1 and zed2 which
    uh we have variable zed 1 and zed2 which

    correspond to slantness and neatness correspond to slantness and neatness correspond
    to slantness and neatness

    respectively. So zed 1 controls the tilt and zed 2 So zed 1 controls the tilt
    and zed 2

    controls the neatness. controls the neatness. controls the neatness.

    We pass this to the decoder which was We pass this to the decoder which was We
    pass this to the decoder which was

    also called as a machine in the also called as a machine in the also called as
    a machine in the

    introduction and then we generate the introduction and then we generate the introduction
    and then we generate the

    actual handwriting. The decoder is quite actual handwriting. The decoder is quite
    actual handwriting. The decoder is quite

    commonly a neural network commonly a neural network commonly a neural network

    and depending on where your sample is in and depending on where your sample is
    in and depending on where your sample is in

    the Latin space, your handwriting will the Latin space, your handwriting will
    the Latin space, your handwriting will

    vary. So here you can see that as the vary. So here you can see that as the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 21
  start_sec: 1304.72
  end_sec: 1364.24
  text: 'vary. So here you can see that as the

    yellow dot moves around the Latin space, yellow dot moves around the Latin space,
    yellow dot moves around the Latin space,

    the handwriting on the right hand side the handwriting on the right hand side
    the handwriting on the right hand side

    also changes. also changes. also changes.

    And this is the architecture of the And this is the architecture of the And this
    is the architecture of the

    machine that we have constructed. machine that we have constructed. machine that
    we have constructed.

    So people asked us to generate a machine So people asked us to generate a machine
    So people asked us to generate a machine

    which gives the handwriting. So we gave which gives the handwriting. So we gave
    which gives the handwriting. So we gave

    them a machine and we gave them two them a machine and we gave them two them a
    machine and we gave them two

    levers. One lever to control the levers. One lever to control the levers. One
    lever to control the

    slantness, one lever to control the slantness, one lever to control the slantness,
    one lever to control the

    neatness. They have to pull these levers neatness. They have to pull these levers
    neatness. They have to pull these levers

    and finally they''ll get a paper with a and finally they''ll get a paper with
    a and finally they''ll get a paper with a

    handwriting written on it. handwriting written on it. handwriting written on it.

    Now the question is that after people Now the question is that after people Now
    the question is that after people

    pull the levers what is exactly pull the levers what is exactly pull the levers
    what is exactly

    happening in the machine that is giving happening in the machine that is giving
    happening in the machine that is giving

    them the handwriting? them the handwriting? them the handwriting?

    What''s what''s exactly happening inside What''s what''s exactly happening inside
    What''s what''s exactly happening inside

    this magical machine box? this magical machine box? this magical machine box?

    How how does the decoder exactly work? Okay. So uh that is the question we ask
    Okay. So uh that is the question we ask

    next. So far we have used the decoder to next. So far we have used the decoder
    to'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 22
  start_sec: 1364.24
  end_sec: 1435.679
  text: 'next. So far we have used the decoder to

    generate samples from the latent generate samples from the latent generate samples
    from the latent

    variables. But what is this decoder variables. But what is this decoder variables.
    But what is this decoder

    exactly and how are the samples exactly and how are the samples exactly and how
    are the samples

    generated generated generated

    from this decoder? from this decoder? from this decoder?

    So now we are going to take a second So now we are going to take a second So now
    we are going to take a second

    example. Instead of generating example. Instead of generating example. Instead
    of generating

    handwriting samples our task now is to handwriting samples our task now is to
    handwriting samples our task now is to

    generate handwritten digits. generate handwritten digits. generate handwritten
    digits.

    What are handwritten digits? We are What are handwritten digits? We are What are
    handwritten digits? We are

    going to take example of Mnest digits going to take example of Mnest digits going
    to take example of Mnest digits

    which look as follows. So these are a famous data set of So these are a famous
    data set of

    handwritten digit samples. handwritten digit samples. handwritten digit samples.

    So our task now is to So our task now is to So our task now is to

    you know generate these digits you know generate these digits you know generate
    these digits

    and again we start with a very same and again we start with a very same and again
    we start with a very same

    thinking process. We try to understand thinking process. We try to understand
    thinking process. We try to understand

    okay fine now we have moved on from okay fine now we have moved on from okay fine
    now we have moved on from

    letters to digits. So we''ll use the same letters to digits. So we''ll use the
    same letters to digits. So we''ll use the same

    thinking process. What are the hidden thinking process. What are the hidden thinking
    process. What are the hidden

    factors that determine the shape of the factors that determine the shape of the
    factors that determine the shape of the

    handwritten digits handwritten digits handwritten digits

    and and and

    we create a latent space with the latent we create a latent space with the latent'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 23
  start_sec: 1435.679
  end_sec: 1494.96
  text: 'we create a latent space with the latent

    variables. So just as before we assume variables. So just as before we assume
    variables. So just as before we assume

    that there are two latent variables zed that there are two latent variables zed
    that there are two latent variables zed

    1 and zed 2 1 and zed 2 1 and zed 2

    and we assume that these two latent and we assume that these two latent and we
    assume that these two latent

    variables are used to determine the variables are used to determine the variables
    are used to determine the

    shape of the handwritten digit. [snorts] shape of the handwritten digit. [snorts]
    shape of the handwritten digit. [snorts]

    Now one difference in this use case Now one difference in this use case Now one
    difference in this use case

    compared to previous use case is that we compared to previous use case is that
    we compared to previous use case is that we

    do not know what these latent variables do not know what these latent variables
    do not know what these latent variables

    correspond to which is quite realistic. correspond to which is quite realistic.
    correspond to which is quite realistic.

    In in reality we have absolutely no idea In in reality we have absolutely no idea
    In in reality we have absolutely no idea

    what factors determine the shape of the what factors determine the shape of the
    what factors determine the shape of the

    handwritten digits and this is something handwritten digits and this is something
    handwritten digits and this is something

    which neural networks really excel at which neural networks really excel at which
    neural networks really excel at

    because they are able to learn these because they are able to learn these because
    they are able to learn these

    hidden factors and we can''t really hidden factors and we can''t really hidden
    factors and we can''t really

    comprehend them what they are. There comprehend them what they are. There comprehend
    them what they are. There

    might be some function of the thickness, might be some function of the thickness,
    might be some function of the thickness,

    slantness, curve, everything. But slantness, curve, everything. But slantness,
    curve, everything. But

    somehow they capture it. That''s all we somehow they capture it. That''s all we
    somehow they capture it. That''s all we

    know. [snorts] know. [snorts]'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 24
  start_sec: 1494.96
  end_sec: 1556.95
  text: 'know. [snorts]

    Now let''s say we have chosen a point in Now let''s say we have chosen a point
    in Now let''s say we have chosen a point in

    the Latin space which corresponds to the the Latin space which corresponds to
    the the Latin space which corresponds to the

    number five. number five. number five.

    The main question we are asking is that The main question we are asking is that
    The main question we are asking is that

    how do we go from a point in the Latin how do we go from a point in the Latin
    how do we go from a point in the Latin

    space space space

    to to to

    a point in the real space? That is how a point in the real space? That is how
    a point in the real space? That is how

    do we generate an actual sample from a do we generate an actual sample from a
    do we generate an actual sample from a

    point in the Latin space? point in the Latin space? point in the Latin space?

    How do we generate the actual sample for How do we generate the actual sample
    for How do we generate the actual sample for

    the digit five? Once we pass this to the the digit five? Once we pass this to
    the the digit five? Once we pass this to the

    decoder, that''s what we are trying to decoder, that''s what we are trying to
    decoder, that''s what we are trying to

    understand. understand. understand.

    Once we pass this to the decoder, we Once we pass this to the decoder, we Once
    we pass this to the decoder, we

    want to generate this five. But what is want to generate this five. But what is
    want to generate this five. But what is

    exactly happening in this decoder? So let''s understand. First we look at So let''s
    understand. First we look at

    what exactly is this image five? What what exactly is this image five? What what
    exactly is this image five? What

    [snorts] what does it mean? We have [snorts] what does it mean? We have [snorts]
    what does it mean? We have

    already briefly looked at it. But already briefly looked at it. But already briefly
    looked at it. But

    we can represent digit 5 as a bunch of'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 25
  start_sec: 1556.95
  end_sec: 1628.799
  text: 'we can represent digit 5 as a bunch of we can represent digit 5 as a bunch
    of

    pixels pixels pixels

    which are divided as 28 into 28 pixels where some pixels have a value of where
    some pixels have a value of

    1. 1. 1.

    which is which is the color white and which is which is the color white and which
    is which is the color white and

    some pixels has the have have the value some pixels has the have have the value
    some pixels has the have have the value

    of zero which is the color black. of zero which is the color black. of zero which
    is the color black.

    So what we do is we have a grid of 788 So what we do is we have a grid of 788
    So what we do is we have a grid of 788

    squares and we assign one value to each squares and we assign one value to each
    squares and we assign one value to each

    square in the grid square in the grid square in the grid

    and this corresponds to the image five. So for example uh this is how we can So
    for example uh this is how we can

    represent five. It it it looks like a represent five. It it it looks like a represent
    five. It it it looks like a

    slanted five and the handwriting is not slanted five and the handwriting is not
    slanted five and the handwriting is not

    very good. But very good. But very good. But

    uh what I''m trying to convey here is uh what I''m trying to convey here is uh
    what I''m trying to convey here is

    that every pixel is assigned a value of that every pixel is assigned a value of
    that every pixel is assigned a value of

    0 or one where white pixels correspond 0 or one where white pixels correspond
    0 or one where white pixels correspond

    to one and black pixels correspond to to one and black pixels correspond to to
    one and black pixels correspond to

    zero. And you can see how the digit zero. And you can see how the digit zero.
    And you can see how the digit

    five, if you closely look at it, it it five, if you closely look at it, it it'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 26
  start_sec: 1628.799
  end_sec: 1688.48
  text: 'five, if you closely look at it, it it

    does look like a five. It''s it''s it''s does look like a five. It''s it''s it''s
    does look like a five. It''s it''s it''s

    almost something like this. Okay. So it looks like all we have to do Okay. So
    it looks like all we have to do

    is output a number either zero or one at is output a number either zero or one
    at is output a number either zero or one at

    the appropriate location so that we get the appropriate location so that we get
    the appropriate location so that we get

    a shape five. a shape five. a shape five.

    And And And

    we can in fact stop this discussion of we can in fact stop this discussion of
    we can in fact stop this discussion of

    how decoder works at this point. But in how decoder works at this point. But in
    how decoder works at this point. But in

    in most of the real life cases, for in most of the real life cases, for in most
    of the real life cases, for

    example, when you are trying to generate example, when you are trying to generate
    example, when you are trying to generate

    images using popular apps like images using popular apps like images using popular
    apps like

    midjourney or stable diffusion, you midjourney or stable diffusion, you midjourney
    or stable diffusion, you

    generally see that for the same prompt, generally see that for the same prompt,
    generally see that for the same prompt,

    you get different type of images. Why is you get different type of images. Why
    is you get different type of images. Why is

    that the case? that the case? that the case?

    because in most of these cases the because in most of these cases the because
    in most of these cases the

    output is not deterministic but it is output is not deterministic but it is output
    is not deterministic but it is

    rather probabilistic. rather probabilistic. rather probabilistic.

    So uh So uh So uh

    one one drawback of this above approach one one drawback of this above approach
    one one drawback of this above approach

    is that with this approach we will get a is that with this approach we will get
    a'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 27
  start_sec: 1688.48
  end_sec: 1750.159
  text: 'is that with this approach we will get a

    fixed shape of five every time but we fixed shape of five every time but we fixed
    shape of five every time but we

    will not get variations of it and what will not get variations of it and what
    will not get variations of it and what

    we want is we want to get variations of we want is we want to get variations of
    we want is we want to get variations of

    the number five. So instead of outputting a single So instead of outputting a
    single

    number, what if you could output a number, what if you could output a number,
    what if you could output a

    probability density? probability density? probability density?

    What does that mean? So we''ll again take What does that mean? So we''ll again
    take What does that mean? So we''ll again take

    the same example of the number five, but the same example of the number five,
    but the same example of the number five, but

    now for every pixel instead of now for every pixel instead of now for every pixel
    instead of

    outputting one number, we output a outputting one number, we output a outputting
    one number, we output a

    probability density. For example, for probability density. For example, for probability
    density. For example, for

    this black, you can see that the mean is this black, you can see that the mean
    is this black, you can see that the mean is

    still zero, but there is some deviation. still zero, but there is some deviation.
    still zero, but there is some deviation.

    Also for this pixel which corresp which Also for this pixel which corresp which
    Also for this pixel which corresp which

    which which is white in color you can which which is white in color you can which
    which is white in color you can

    see that the mean is one but there is see that the mean is one but there is see
    that the mean is one but there is

    some deviation some deviation some deviation

    which means that you are not just now which means that you are not just now which
    means that you are not just now

    restricted to zero and one. You are open restricted to zero and one. You are open'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 28
  start_sec: 1750.159
  end_sec: 1808.96
  text: 'restricted to zero and one. You are open

    to the possibility of to the possibility of to the possibility of

    a color which appears in between white a color which appears in between white
    a color which appears in between white

    and black slightly grayish. and black slightly grayish. and black slightly grayish.

    [snorts] [snorts]

    So this is what the alternative So this is what the alternative So this is what
    the alternative

    representation as a probability density representation as a probability density
    representation as a probability density

    allows you to do. allows you to do. allows you to do.

    Now what happens is that every time for Now what happens is that every time for
    Now what happens is that every time for

    each pixel you will sample from this each pixel you will sample from this each
    pixel you will sample from this

    distribution. So one time you might get distribution. So one time you might get
    distribution. So one time you might get

    this, one time you might get this. It this, one time you might get this. It this,
    one time you might get this. It

    will still have a mean of zero. So it will still have a mean of zero. So it will
    still have a mean of zero. So it

    will still look mostly black but you will still look mostly black but you will
    still look mostly black but you

    will get variations of it. will get variations of it. will get variations of it.

    And uh we will see this in in a more And uh we will see this in in a more And
    uh we will see this in in a more

    practical example. But this is what practical example. But this is what practical
    example. But this is what

    happens uh [snorts] happens uh [snorts] happens uh [snorts]

    in a in a in a

    in in in a actual practical example in in in a actual practical example in in
    in a actual practical example

    where you want to see different images where you want to see different images
    where you want to see different images

    generated from the decoder. So the the generated from the decoder. So the the
    generated from the decoder. So the the

    the decoder does not give a single value the decoder does not give a single value'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 29
  start_sec: 1808.96
  end_sec: 1873.2
  text: 'the decoder does not give a single value

    but for every pixel the decoder gives but for every pixel the decoder gives but
    for every pixel the decoder gives

    the mean the mean the mean

    and the standard deviation and the standard deviation and the standard deviation

    for this probability distribution. So I think I have just I I''ll just move So
    I think I have just I I''ll just move

    down a little bit to help you understand down a little bit to help you understand
    down a little bit to help you understand

    how this looks like. how this looks like. how this looks like.

    So So

    this is what the decoder does. So for this is what the decoder does. So for this
    is what the decoder does. So for

    every pixel you get a mean and a every pixel you get a mean and a every pixel
    you get a mean and a

    standard deviation. So you have mu1 standard deviation. So you have mu1 standard
    deviation. So you have mu1

    sigma 1 mu2 sigma 2 up to mu 784 sigma sigma 1 mu2 sigma 2 up to mu 784 sigma
    sigma 1 mu2 sigma 2 up to mu 784 sigma

    784 and that''s why you get different samples and that''s why you get different
    samples

    towards the end. towards the end. towards the end.

    >> [snorts] >> [snorts] >> [snorts]

    >> If you found this a little bit difficult >> If you found this a little bit
    difficult >> If you found this a little bit difficult

    to understand, no worries. You can stick to understand, no worries. You can stick
    to understand, no worries. You can stick

    with this deterministic approach which I with this deterministic approach which
    I with this deterministic approach which I

    explained a while back because this is explained a while back because this is
    explained a while back because this is

    also a valid solution. In fact, in the also a valid solution. In fact, in the
    also a valid solution. In fact, in the

    practical sol uh example which we are practical sol uh example which we are practical
    sol uh example which we are

    going to discuss today, we use a going to discuss today, we use a going to discuss
    today, we use a

    deterministic approach only. deterministic approach only.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 30
  start_sec: 1873.2
  end_sec: 1936.32
  text: 'deterministic approach only.

    So now let us So now let us So now let us

    have a simple example to understand how have a simple example to understand how
    have a simple example to understand how

    does the decoder work. does the decoder work. does the decoder work.

    Uh Uh Uh

    to quickly summarize, a decoder is to quickly summarize, a decoder is to quickly
    summarize, a decoder is

    a function which gives you an output at a function which gives you an output at
    a function which gives you an output at

    the end which can either be a simple the end which can either be a simple the
    end which can either be a simple

    number which corresponds to the pixel number which corresponds to the pixel number
    which corresponds to the pixel

    intensity 0 or one or it can be a intensity 0 or one or it can be a intensity
    0 or one or it can be a

    probability density for each pixel. probability density for each pixel. probability
    density for each pixel.

    Now how do we generate this function? Now how do we generate this function? Now
    how do we generate this function?

    Well, function generation typically Well, function generation typically Well,
    function generation typically

    happens with a neural network uh because happens with a neural network uh because
    happens with a neural network uh because

    neural networks really capture the a lot neural networks really capture the a
    lot neural networks really capture the a lot

    of functional distributions really well. of functional distributions really well.
    of functional distributions really well.

    So we use a neural network to take the So we use a neural network to take the
    So we use a neural network to take the

    latin space variables as the input and latin space variables as the input and
    latin space variables as the input and

    then once we have these inputs we then once we have these inputs we then once
    we have these inputs we

    generate outputs for generate outputs for generate outputs for

    uh these inputs using a neural network uh these inputs using a neural network
    uh these inputs using a neural network

    which sits at the center. which sits at the center. which sits at the center.

    So the decoder is nothing but a neural So the decoder is nothing but a neural'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 31
  start_sec: 1936.32
  end_sec: 1991.2
  text: 'So the decoder is nothing but a neural

    network which is trained to take inputs network which is trained to take inputs
    network which is trained to take inputs

    from the latin space and generate from the latin space and generate from the latin
    space and generate

    outputs in the real space. So we are outputs in the real space. So we are outputs
    in the real space. So we are

    going to look at a very nice going to look at a very nice going to look at a very
    nice

    visualization to understand this. Okay. So um I want you to just not focus Okay.
    So um I want you to just not focus

    too much on this encoder part. We are too much on this encoder part. We are too
    much on this encoder part. We are

    going to cover this later. But we''ll going to cover this later. But we''ll going
    to cover this later. But we''ll

    just start from the latent vector zed. just start from the latent vector zed.
    just start from the latent vector zed.

    Assume that we have this latent vector Assume that we have this latent vector
    Assume that we have this latent vector

    zed or z and we want to generate a zed or z and we want to generate a zed or z
    and we want to generate a

    sample. So it goes through the decoder sample. So it goes through the decoder
    sample. So it goes through the decoder

    and then you get the final image. So the and then you get the final image. So
    the and then you get the final image. So the

    decoder predicts pixel probabilities not decoder predicts pixel probabilities
    not decoder predicts pixel probabilities not

    a final image. So what does that mean? a final image. So what does that mean?
    a final image. So what does that mean?

    [snorts] Let''s see. [snorts] Let''s see. [snorts] Let''s see.

    If you take an example of a white pixel, If you take an example of a white pixel,
    If you take an example of a white pixel,

    you can see that the pixel mean is you can see that the pixel mean is you can
    see that the pixel mean is

    somewhere towards the right, which means somewhere towards the right, which means'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 32
  start_sec: 1991.2
  end_sec: 2050.629
  text: 'somewhere towards the right, which means

    that it has to be a bit bright and the that it has to be a bit bright and the
    that it has to be a bit bright and the

    pixel value is high. Bright pixels have pixel value is high. Bright pixels have
    pixel value is high. Bright pixels have

    a high mean value. But if you take a a high mean value. But if you take a a high
    mean value. But if you take a

    pixel somewhere in the middle or towards pixel somewhere in the middle or towards
    pixel somewhere in the middle or towards

    the blackish side, you can see that it the blackish side, you can see that it
    the blackish side, you can see that it

    moves towards the left. So every pixel moves towards the left. So every pixel
    moves towards the left. So every pixel

    gets a probability distribution like gets a probability distribution like gets
    a probability distribution like

    this through the decoder. And once you this through the decoder. And once you
    this through the decoder. And once you

    have this we we can sample from this have this we we can sample from this have
    this we we can sample from this

    distribution to get various outputs. distribution to get various outputs. distribution
    to get various outputs.

    So that is the main advantage of So that is the main advantage of So that is the
    main advantage of

    assigning probability distributions to assigning probability distributions to
    assigning probability distributions to

    each each pixel. I want all of you to again revisit this I want all of you to
    again revisit this

    after you have seen this entire lecture after you have seen this entire lecture
    after you have seen this entire lecture

    and actually draw a diagram of 28x 28 and actually draw a diagram of 28x 28 and
    actually draw a diagram of 28x 28

    pixels and write down mu1 sigma 1 for pixels and write down mu1 sigma 1 for pixels
    and write down mu1 sigma 1 for

    each and then try to visualize how does each and then try to visualize how does
    each and then try to visualize how does

    the image really look like. the image really look like. the image really look
    like.

    Okay. Um Okay. Um Okay. Um

    now we have covered'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 33
  start_sec: 2050.629
  end_sec: 2110.079
  text: 'now we have covered now we have covered

    one part of the story which explains the one part of the story which explains
    the one part of the story which explains the

    variational autoenccoder. variational autoenccoder. variational autoenccoder.

    What about What about What about

    the second half of the story? So we have the second half of the story? So we have
    the second half of the story? So we have

    just covered 50% of the entire story. just covered 50% of the entire story. just
    covered 50% of the entire story.

    Let''s let''s try to cover the second part Let''s let''s try to cover the second
    part Let''s let''s try to cover the second part

    so that we get a complete picture of how so that we get a complete picture of
    how so that we get a complete picture of how

    the variational autoenccoder works. the variational autoenccoder works. the variational
    autoenccoder works.

    And some of you might be having this And some of you might be having this And
    some of you might be having this

    question at the back of your mind that where does the word variational come where
    does the word variational come

    from and how is this different from a from and how is this different from a from
    and how is this different from a

    pure autoenccoder and u why was it why did it become so and u why was it why did
    it become so

    popular when it came into the scene popular when it came into the scene popular
    when it came into the scene

    [snorts] [snorts]

    and where is the encoder? So there there and where is the encoder? So there there
    and where is the encoder? So there there

    might be a lot of questions in your might be a lot of questions in your might
    be a lot of questions in your

    mind. So let''s let''s understand that mind. So let''s let''s understand that
    mind. So let''s let''s understand that

    that in in this second part. that in in this second part. that in in this second
    part.

    If you paid close attention to the first If you paid close attention to the first
    If you paid close attention to the first

    part, you will understand that we have part, you will understand that we have'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 34
  start_sec: 2110.079
  end_sec: 2174.96
  text: 'part, you will understand that we have

    made a major assumption. made a major assumption. made a major assumption.

    Remember when we talked about the Remember when we talked about the Remember when
    we talked about the

    handwritten digit five here, we said that let us assume this here, we said that
    let us assume this

    part of the Latin space corresponds to part of the Latin space corresponds to
    part of the Latin space corresponds to

    the digit five. [clears throat] the digit five. [clears throat] the digit five.
    [clears throat]

    How did we make this assumption? How did we make this assumption? How did we make
    this assumption?

    How do we know where does the digit five How do we know where does the digit five
    How do we know where does the digit five

    lie in the Latin space? It can be here. lie in the Latin space? It can be here.
    lie in the Latin space? It can be here.

    It can be here. It can be anywhere. It can be here. It can be anywhere. It can
    be here. It can be anywhere.

    Right? How do we know the digit five is Right? How do we know the digit five is
    Right? How do we know the digit five is

    where it''s drawn on the screen right? So how do we generate this distribution
    So how do we generate this distribution

    in the Latin space in the Latin space in the Latin space

    which is it it looks like something not which is it it looks like something not
    which is it it looks like something not

    straightforward right? Look at the straightforward right? Look at the straightforward
    right? Look at the

    example of students in your class example of students in your class example of
    students in your class

    writing the word hello. To generate the writing the word hello. To generate the
    writing the word hello. To generate the

    distribution in the Latin space, distribution in the Latin space, distribution
    in the Latin space,

    you need to first understand all the you need to first understand all the you
    need to first understand all the

    underlying hidden factors of the secret underlying hidden factors of the secret
    underlying hidden factors of the secret

    recipe and then you need to map all recipe and then you need to map all'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 35
  start_sec: 2174.96
  end_sec: 2233.589
  text: 'recipe and then you need to map all

    these handwriting styles to the secret these handwriting styles to the secret
    these handwriting styles to the secret

    recipe and make all those points and recipe and make all those points and recipe
    and make all those points and

    then generate this distribution in the then generate this distribution in the
    then generate this distribution in the

    Latin space. It looks like a big task Latin space. It looks like a big task Latin
    space. It looks like a big task

    which we have taken for granted. which we have taken for granted. which we have
    taken for granted.

    In other words, how is this compression In other words, how is this compression
    In other words, how is this compression

    happening from the real space to the happening from the real space to the happening
    from the real space to the

    latent space? How are we able to latent space? How are we able to latent space?
    How are we able to

    compress the data so much? And who is compress the data so much? And who is compress
    the data so much? And who is

    doing this compression? So, uh how do we know which part of the So, uh how do
    we know which part of the

    latin space to access to generate the latin space to access to generate the latin
    space to access to generate the

    digit five? digit five? digit five?

    [snorts] [snorts]

    Uh and this is exactly what the encoder Uh and this is exactly what the encoder
    Uh and this is exactly what the encoder

    does. The encoder takes an input image does. The encoder takes an input image
    does. The encoder takes an input image

    and compresses it into the latin space. and compresses it into the latin space.
    and compresses it into the latin space.

    So one option is to access all possible So one option is to access all possible
    So one option is to access all possible

    points. So for example to answer this points. So for example to answer this points.
    So for example to answer this

    question of how do we know which part of question of how do we know which part
    of question of how do we know which part of

    the latin space to access to generate'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 36
  start_sec: 2233.589
  end_sec: 2284.16
  text: 'the latin space to access to generate the latin space to access to generate

    digit five. One option is to access all digit five. One option is to access all
    digit five. One option is to access all

    possible points in the latent space and possible points in the latent space and
    possible points in the latent space and

    see which images match closely to the see which images match closely to the see
    which images match closely to the

    digit five. So for example what you do digit five. So for example what you do
    digit five. So for example what you do

    is you take this pass it through the is you take this pass it through the is you
    take this pass it through the

    decoder see what image is generated take decoder see what image is generated take
    decoder see what image is generated take

    this take this take this this take this take this this take this take this

    is this a good solution is this a good solution is this a good solution

    it''s not a good solution because it''s it''s not a good solution because it''s
    it''s not a good solution because it''s

    completely intractable you have to completely intractable you have to completely
    intractable you have to

    sample all the points in the latin space sample all the points in the latin space
    sample all the points in the latin space

    and then you finally realize okay these and then you finally realize okay these
    and then you finally realize okay these

    this is the region which is you know this is the region which is you know this
    is the region which is you know

    giving me the sample which correspond giving me the sample which correspond giving
    me the sample which correspond

    responds to the digit five. responds to the digit five. responds to the digit
    five.

    It appears like we have to do a lot of It appears like we have to do a lot of
    It appears like we have to do a lot of

    work. It''s almost like finding a needle work. It''s almost like finding a needle
    work. It''s almost like finding a needle

    in a haststack. in a haststack. in a haststack.

    Wouldn''t it be better if we knew which Wouldn''t it be better if we knew which'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 37
  start_sec: 2284.16
  end_sec: 2340.72
  text: 'Wouldn''t it be better if we knew which

    part of the Latin space to access for part of the Latin space to access for part
    of the Latin space to access for

    the type of image we want to generate? the type of image we want to generate?
    the type of image we want to generate?

    It''ll be great if someone told me this It''ll be great if someone told me this
    It''ll be great if someone told me this

    is is is

    a region for five. This is the region a region for five. This is the region a
    region for five. This is the region

    where you will get numbers corresponding where you will get numbers corresponding
    where you will get numbers corresponding

    to one. This is the region where you to one. This is the region where you to one.
    This is the region where you

    will get numbers corresponding to two will get numbers corresponding to two will
    get numbers corresponding to two

    etc. etc. etc.

    So I want the spaces in my Latin space So I want the spaces in my Latin space
    So I want the spaces in my Latin space

    to actually mean something and to to actually mean something and to to actually
    mean something and to

    correspond to some you know information. correspond to some you know information.
    correspond to some you know information.

    So wouldn''t it be great if we build So wouldn''t it be great if we build So wouldn''t
    it be great if we build

    another machine to do that? So I give my another machine to do that? So I give
    my another machine to do that? So I give my

    input image which is the digit I want to input image which is the digit I want
    to input image which is the digit I want to

    generate five. It goes through another generate five. It goes through another
    generate five. It goes through another

    machine which gives me the areas of the machine which gives me the areas of the
    machine which gives me the areas of the

    latin space corresponding to that input latin space corresponding to that input
    latin space corresponding to that input

    image and then I pass this to the image and then I pass this to the image and
    then I pass this to the

    decoder. decoder.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 38
  start_sec: 2340.72
  end_sec: 2400.32
  text: 'decoder.

    So the overall architecture looks like So the overall architecture looks like
    So the overall architecture looks like

    this. this. this.

    First I get let''s say you go to any First I get let''s say you go to any First
    I get let''s say you go to any

    student of your class take the sheet of student of your class take the sheet of
    student of your class take the sheet of

    their handwriting sample hello their handwriting sample hello their handwriting
    sample hello

    you pass that handwriting sample to one you pass that handwriting sample to one
    you pass that handwriting sample to one

    machine machine machine

    that machine gives you the levers which that machine gives you the levers which
    that machine gives you the levers which

    lever I''m supposed to pull lever I''m supposed to pull lever I''m supposed to
    pull

    then you pull those levers in the secret then you pull those levers in the secret
    then you pull those levers in the secret

    recipe recipe recipe

    and then the decoder does its magic and and then the decoder does its magic and
    and then the decoder does its magic and

    you get the final output. you get the final output. you get the final output.

    So uh let''s say I have these two levers So uh let''s say I have these two levers
    So uh let''s say I have these two levers

    in my hand which I want to pull. in my hand which I want to pull. in my hand which
    I want to pull.

    The first part the first machine tells The first part the first machine tells
    The first part the first machine tells

    me which levers to pull and then I pull me which levers to pull and then I pull
    me which levers to pull and then I pull

    the levers and I get the output. the levers and I get the output. the levers and
    I get the output.

    So this machine which is telling me So this machine which is telling me So this
    machine which is telling me

    which levers to pull is also called as which levers to pull is also called as
    which levers to pull is also called as

    the encoder. Now Now

    this architecture is very similar to a this architecture is very similar to a'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 39
  start_sec: 2400.32
  end_sec: 2463.19
  text: 'this architecture is very similar to a

    plain autoenccoder where you have an plain autoenccoder where you have an plain
    autoenccoder where you have an

    encoder which compresses the image into encoder which compresses the image into
    encoder which compresses the image into

    a latin space and you decode it into the a latin space and you decode it into
    the a latin space and you decode it into the

    real space. real space. real space.

    But where is the you know variational But where is the you know variational But
    where is the you know variational

    part of it coming into the picture part of it coming into the picture part of
    it coming into the picture

    really? Why is it called a variational really? Why is it called a variational
    really? Why is it called a variational

    autoenccoder? autoenccoder? autoenccoder?

    Why is the encoder even necessary? Why is the encoder even necessary? Why is the
    encoder even necessary?

    Um I mean why is the variational part of Um I mean why is the variational part
    of Um I mean why is the variational part of

    the encoder necessary? the encoder necessary? the encoder necessary?

    >> [snorts] >> [snorts]

    >> So >> So >> So

    okay in in pure autoenccoders what okay in in pure autoenccoders what okay in
    in pure autoenccoders what

    happened was that happened was that happened was that

    for every image which was passed to this for every image which was passed to this
    for every image which was passed to this

    machine you got a single point machine you got a single point machine you got
    a single point

    you got this point corresponding to five you got this point corresponding to five
    you got this point corresponding to five

    this point corresponding to one this this point corresponding to one this this
    point corresponding to one this

    point corresponding to two this point point corresponding to two this point point
    corresponding to two this point

    corresponding to three. What variational corresponding to three. What variational
    corresponding to three. What variational

    autoenccoders did was they did not give autoenccoders did was they did not give
    autoenccoders did was they did not give

    a point as the output but they gave a point as the output but they gave a point
    as the output but they gave

    a dis or or a region which is the most'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 40
  start_sec: 2463.19
  end_sec: 2521.829
  text: 'a dis or or a region which is the most a dis or or a region which is the
    most

    probable region of finding the digit probable region of finding the digit probable
    region of finding the digit

    five instead of just giving a single five instead of just giving a single five
    instead of just giving a single

    point as the output. That''s why the word variational comes. That''s why the word
    variational comes.

    You don''t get a single single You don''t get a single single You don''t get a
    single single

    deterministic output from the encoder deterministic output from the encoder deterministic
    output from the encoder

    but rather you get this region of space but rather you get this region of space
    but rather you get this region of space

    where the encoder tells you that this is where the encoder tells you that this
    is where the encoder tells you that this is

    the mean. This is where you are most the mean. This is where you are most the
    mean. This is where you are most

    likely to find it but this is the likely to find it but this is the likely to
    find it but this is the

    broader space where broader space where broader space where

    the probability decreases but you will the probability decreases but you will
    the probability decreases but you will

    still find it. You still have a chance still find it. You still have a chance
    still find it. You still have a chance

    to find it. to find it. to find it.

    And And

    this you know this was this you know this was this you know this was

    very very very

    uh I would say powerful at that time and uh I would say powerful at that time
    and uh I would say powerful at that time and

    and and it led to and and it led to and and it led to

    image generation which people had not image generation which people had not image
    generation which people had not

    seen before. It''s not very intuitive why seen before. It''s not very intuitive
    why seen before. It''s not very intuitive why

    the variational part works so well but the variational part works so well but
    the variational part works so well but

    we are going to look at a nice visual'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 41
  start_sec: 2521.829
  end_sec: 2592.48
  text: 'we are going to look at a nice visual we are going to look at a nice visual

    description to understand this much description to understand this much description
    to understand this much

    better. better. better.

    So I I myself was trying to understand So I I myself was trying to understand
    So I I myself was trying to understand

    this for a for quite some time but then this for a for quite some time but then
    this for a for quite some time but then

    I came up with this visual explanation I came up with this visual explanation
    I came up with this visual explanation

    so that so that so that

    I I''m able to explain you the thought I I''m able to explain you the thought
    I I''m able to explain you the thought

    process in my mind. Okay. So Okay. So

    we know that the decoder learns to map we know that the decoder learns to map
    we know that the decoder learns to map

    specific points to specific regions. For specific points to specific regions.
    For specific points to specific regions. For

    example, this blue point corresponds to example, this blue point corresponds to
    example, this blue point corresponds to

    dog and it memorizes that okay - 3a 2 is dog and it memorizes that okay - 3a 2
    is dog and it memorizes that okay - 3a 2 is

    a dog and 3 - 3 is a cat. This is what a dog and 3 - 3 is a cat. This is what
    a dog and 3 - 3 is a cat. This is what

    pure autoenccoders did. They memorized pure autoenccoders did. They memorized
    pure autoenccoders did. They memorized

    each point corresponds to a specific each point corresponds to a specific each
    point corresponds to a specific

    image. Now the question is what lies between Now the question is what lies between

    these points? these points? these points?

    It''s it''s not clear, right? It can be It''s it''s not clear, right? It can be
    It''s it''s not clear, right? It can be

    anything. So inside these points, it''s largely So inside these points, it''s
    largely

    noise because you have only mapped noise because you have only mapped noise because
    you have only mapped

    individual points. So 99% of these individual points. So 99% of these'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 42
  start_sec: 2592.48
  end_sec: 2654.24
  text: 'individual points. So 99% of these

    points, they they produce garbage. So points, they they produce garbage. So points,
    they they produce garbage. So

    your your space your latent space is not your your space your latent space is
    not your your space your latent space is not

    continuous. It''s like disjoint. continuous. It''s like disjoint. continuous.
    It''s like disjoint.

    [snorts] This this creates a mathematical This this creates a mathematical

    disaster. disaster. disaster.

    Uh to generate a dog, we need to look at Uh to generate a dog, we need to look
    at Uh to generate a dog, we need to look at

    all possible points in this space and all possible points in this space and all
    possible points in this space and

    then add up every single then add up every single then add up every single

    uh every single point and try to map it uh every single point and try to map it
    uh every single point and try to map it

    to the output and then we know that okay to the output and then we know that okay
    to the output and then we know that okay

    fine this is the region which produces a fine this is the region which produces
    a fine this is the region which produces a

    dog. So as we discussed before this is dog. So as we discussed before this is
    dog. So as we discussed before this is

    completely intractable. So you can''t really you know search So you can''t really
    you know search

    blindly in an infinite ocean to find out blindly in an infinite ocean to find
    out blindly in an infinite ocean to find out

    where is the dog exactly. where is the dog exactly. where is the dog exactly.

    We can''t integrate over the entire We can''t integrate over the entire We can''t
    integrate over the entire

    universe. It is not tractable. In other universe. It is not tractable. In other
    universe. It is not tractable. In other

    words, you need regions of spaces in words, you need regions of spaces in words,
    you need regions of spaces in

    your latent space. You need continuous your latent space. You need continuous
    your latent space. You need continuous

    regions which tell you that this is the regions which tell you that this is the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 43
  start_sec: 2654.24
  end_sec: 2708.79
  text: 'regions which tell you that this is the

    region corresponding to the dog. This is region corresponding to the dog. This
    is region corresponding to the dog. This is

    the region corresponding to the cat etc. And we need a guide which is the And
    we need a guide which is the

    encoder. encoder. encoder.

    What the encoder does is that it if you What the encoder does is that it if you
    What the encoder does is that it if you

    give an input which is a dog, it tells give an input which is a dog, it tells
    give an input which is a dog, it tells

    you that this is the region where you you that this is the region where you you
    that this is the region where you

    are most likely to find a dog. It tells are most likely to find a dog. It tells
    are most likely to find a dog. It tells

    you that don''t search the entire ocean you that don''t search the entire ocean
    you that don''t search the entire ocean

    but only search this blue region where but only search this blue region where
    but only search this blue region where

    you are most likely to find a dog. It you are most likely to find a dog. It you
    are most likely to find a dog. It

    turns an impossible search into a direct turns an impossible search into a direct
    turns an impossible search into a direct

    lookup. And the variational part of it since you And the variational part of it
    since you

    are not just predicting a point, but you are not just predicting a point, but
    you are not just predicting a point, but you

    are giving a space where you''re saying are giving a space where you''re saying
    are giving a space where you''re saying

    that the dog is most likely to be find that the dog is most likely to be find
    that the dog is most likely to be find

    to be found in this space. These spaces to be found in this space. These spaces
    to be found in this space. These spaces

    tend to overlap and you get a latent tend to overlap and you get a latent tend
    to overlap and you get a latent

    space which is continuous and the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 44
  start_sec: 2708.79
  end_sec: 2767.599
  text: 'space which is continuous and the space which is continuous and the

    garbage gaps are now filled with garbage gaps are now filled with garbage gaps
    are now filled with

    distributions. So now you can safely sample from So now you can safely sample
    from

    anywhere and you have a latent space anywhere and you have a latent space anywhere
    and you have a latent space

    which actually means something. which actually means something. which actually
    means something.

    So the result is a smooth blend. It is So the result is a smooth blend. It is
    So the result is a smooth blend. It is

    not noise. not noise. not noise.

    So the the final architecture looks So the the final architecture looks So the
    the final architecture looks

    quite similar to an autoenccoder where quite similar to an autoenccoder where
    quite similar to an autoenccoder where

    you have a machine which gives you which you have a machine which gives you which
    you have a machine which gives you which

    levers to pull but then you don''t get levers to pull but then you don''t get
    levers to pull but then you don''t get

    deterministic values that pull five and deterministic values that pull five and
    deterministic values that pull five and

    pull three but you get a distribution. pull three but you get a distribution.
    pull three but you get a distribution.

    So every time we''ll be pull you''ll be So every time we''ll be pull you''ll be
    So every time we''ll be pull you''ll be

    pulling levers to a different extent. pulling levers to a different extent. pulling
    levers to a different extent.

    Um and Um and Um and

    if if you are if you''re confused why is if if you are if you''re confused why
    is if if you are if you''re confused why is

    this the case try to think about it in this the case try to think about it in
    this the case try to think about it in

    this visual space which I demonstrated this visual space which I demonstrated
    this visual space which I demonstrated

    right now which makes the explanation a right now which makes the explanation
    a right now which makes the explanation a

    bit more clearer. bit more clearer. bit more clearer.

    So the two stories put together form the So the two stories put together form
    the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 45
  start_sec: 2767.599
  end_sec: 2823.04
  text: 'So the two stories put together form the

    variational autoenccoder. variational autoenccoder.

    We first looked at the decoder where we We first looked at the decoder where we
    We first looked at the decoder where we

    saw that we build a machine which can saw that we build a machine which can saw
    that we build a machine which can

    take the hidden factors behind the take the hidden factors behind the take the
    hidden factors behind the

    handwriting styles of the students and handwriting styles of the students and
    handwriting styles of the students and

    then generate then generate then generate

    samples for those hidden factors which samples for those hidden factors which
    samples for those hidden factors which

    we also called as secret recipe. Now we also called as secret recipe. Now we also
    called as secret recipe. Now

    that machine which has the hidden that machine which has the hidden that machine
    which has the hidden

    factors as the levers is called as the factors as the levers is called as the
    factors as the levers is called as the

    decoder and it is also decoder and it is also decoder and it is also

    it is it is a neural network or a it is it is a neural network or a it is it is
    a neural network or a

    function or a mapping which takes the function or a mapping which takes the function
    or a mapping which takes the

    latent variables as the input and gives latent variables as the input and gives
    latent variables as the input and gives

    you the output image. you the output image. you the output image.

    This output image can be a single value This output image can be a single value
    This output image can be a single value

    for each pixel or it can be a for each pixel or it can be a for each pixel or
    it can be a

    probability distribution for each pixel. probability distribution for each pixel.
    probability distribution for each pixel.

    But the question is that how do you get But the question is that how do you get
    But the question is that how do you get

    the areas in the latin space? How do you the areas in the latin space? How do
    you'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 46
  start_sec: 2823.04
  end_sec: 2888.15
  text: 'the areas in the latin space? How do you

    know which levers to pull in the know which levers to pull in the know which levers
    to pull in the

    decoder? This is given to you by the decoder? This is given to you by the decoder?
    This is given to you by the

    encoder. You don''t get deterministic encoder. You don''t get deterministic encoder.
    You don''t get deterministic

    values for these livers, but you get a values for these livers, but you get a
    values for these livers, but you get a

    distribution. You you get a mean and a distribution. You you get a mean and a
    distribution. You you get a mean and a

    variance for the livers to be pulled. variance for the livers to be pulled. variance
    for the livers to be pulled.

    And this is important because finally And this is important because finally And
    this is important because finally

    you get a Latin space which means you get a Latin space which means you get a
    Latin space which means

    something which has some semantic something which has some semantic something
    which has some semantic

    meaning and you don''t get a disjoint meaning and you don''t get a disjoint meaning
    and you don''t get a disjoint

    Latin space but you get a continuous Latin space but you get a continuous Latin
    space but you get a continuous

    Latin space. The encoder and the decoder Latin space. The encoder and the decoder
    Latin space. The encoder and the decoder

    put together form the variational put together form the variational put together
    form the variational

    autoenccoder. Now before we Now before we

    get to the training of variation get to the training of variation get to the training
    of variation

    autoenccoders, let us autoenccoders, let us autoenccoders, let us

    understand how to represent variational understand how to represent variational
    understand how to represent variational

    autoenccoders formally. autoenccoders formally. autoenccoders formally.

    In variational autoenccoders, we In variational autoenccoders, we In variational
    autoenccoders, we

    distinguish between two type of distinguish between two type of distinguish between
    two type of

    variables. variables.

    The observed variables x which The observed variables x which The observed variables
    x which

    correspond to the data we see. These are correspond to the data we see. These
    are correspond to the data we see. These are

    the handwriting the handwriting

    uh styles of the students when they'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 47
  start_sec: 2888.15
  end_sec: 2949.52
  text: 'uh styles of the students when they uh styles of the students when they

    wrote the word hello or the handwritten wrote the word hello or the handwritten
    wrote the word hello or the handwritten

    digits and the latent variable zed which digits and the latent variable zed which
    digits and the latent variable zed which

    captures the hidden factors of captures the hidden factors of captures the hidden
    factors of

    variation. The decoder distribution is variation. The decoder distribution is
    variation. The decoder distribution is

    given as follows. given as follows. given as follows.

    This is the decoder distribution. It it This is the decoder distribution. It it
    This is the decoder distribution. It it

    reads as probability of X given zed reads as probability of X given zed reads
    as probability of X given zed

    which means that given the latent which means that given the latent which means
    that given the latent

    variables what is the probability of the variables what is the probability of
    the variables what is the probability of the

    output output output

    which is also denoted as P5 of X given which is also denoted as P5 of X given
    which is also denoted as P5 of X given

    Z. Z. Z.

    The encoder distribution is written as The encoder distribution is written as
    The encoder distribution is written as

    follows. Q theta of Z given X which follows. Q theta of Z given X which follows.
    Q theta of Z given X which

    means what is the probability of the means what is the probability of the means
    what is the probability of the

    latent latent latent

    variable variable variable

    given the input image given the input image given the input image

    and this makes sense to the intuition we and this makes sense to the intuition
    we and this makes sense to the intuition we

    have been building. The decoder is going have been building. The decoder is going
    have been building. The decoder is going

    to give you the image given the latent to give you the image given the latent
    to give you the image given the latent

    space distribution and the encoder is space distribution and the encoder is space
    distribution and the encoder is

    going to give you the latent space going to give you the latent space'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 48
  start_sec: 2949.52
  end_sec: 3009.829
  text: 'going to give you the latent space

    distribution given the image. So that''s distribution given the image. So that''s
    distribution given the image. So that''s

    why you see the notation kind of flipped why you see the notation kind of flipped
    why you see the notation kind of flipped

    [snorts] but P and Q are the standard [snorts] but P and Q are the standard [snorts]
    but P and Q are the standard

    notations which are used for the decoder notations which are used for the decoder
    notations which are used for the decoder

    and the encoder. and the encoder. and the encoder.

    The schematic representation is given as The schematic representation is given
    as The schematic representation is given as

    follows. Whenever you see the words follows. Whenever you see the words follows.
    Whenever you see the words

    encoder, decoder and these kind of encoder, decoder and these kind of encoder,
    decoder and these kind of

    diagrams don''t get confused because they diagrams don''t get confused because
    they diagrams don''t get confused because they

    really mean something intuitive. really mean something intuitive. really mean
    something intuitive.

    The encoder captures the hidden factors The encoder captures the hidden factors
    The encoder captures the hidden factors

    which are underlying the image or the which are underlying the image or the which
    are underlying the image or the

    distribution and the decoder takes these distribution and the decoder takes these
    distribution and the decoder takes these

    hidden factors and then generates the hidden factors and then generates the hidden
    factors and then generates the

    output. output. output.

    Uh why do you have these Uh why do you have these Uh why do you have these

    shapes like these shapes like these shapes like these

    gravers? [snorts] The main reason is gravers? [snorts] The main reason is gravers?
    [snorts] The main reason is

    that the encoder compresses the image that the encoder compresses the image that
    the encoder compresses the image

    into the latin space and the decoder into the latin space and the decoder into
    the latin space and the decoder

    brings it back to the original space of brings it back to the original space of
    brings it back to the original space of

    the distribution. So that''s why you have the distribution. So that''s why you
    have the distribution. So that''s why you have

    the encoder like this and the decoder'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 49
  start_sec: 3009.829
  end_sec: 3076.48
  text: 'the encoder like this and the decoder the encoder like this and the decoder

    going from a smaller line here to a going from a smaller line here to a going
    from a smaller line here to a

    bigger line. In in every lecture u I tend to focus on In in every lecture u I
    tend to focus on

    these mathematical notations because these mathematical notations because these
    mathematical notations because

    whenever you read research papers whenever you read research papers whenever you
    read research papers

    you will get to see these notations you will get to see these notations you will
    get to see these notations

    every now and then and uh I just want to every now and then and uh I just want
    to every now and then and uh I just want to

    help you understand that it''s not very help you understand that it''s not very
    help you understand that it''s not very

    difficult but they actually mean difficult but they actually mean difficult but
    they actually mean

    something intuitive whenever you see something intuitive whenever you see something
    intuitive whenever you see

    these notations. these notations. these notations.

    So I''m trying to keep the notations as So I''m trying to keep the notations as
    So I''m trying to keep the notations as

    simple as possible but still I will not simple as possible but still I will not
    simple as possible but still I will not

    shy away from shy away from shy away from

    giving notations and mathematical giving notations and mathematical giving notations
    and mathematical

    intuitions and equations wherever intuitions and equations wherever intuitions
    and equations wherever

    possible because I know it will help you possible because I know it will help
    you possible because I know it will help you

    in your journey to understand diffusion in your journey to understand diffusion
    in your journey to understand diffusion

    models. models. models.

    So uh okay so what I will do is I will uh okay so what I will do is I will uh

    split this lecture into two. In the next split this lecture into two. In the next
    split this lecture into two. In the next

    lecture, I will discuss how exactly are lecture, I will discuss how exactly are
    lecture, I will discuss how exactly are

    these variational autoenccoders trained. these variational autoenccoders trained.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 50
  start_sec: 3076.48
  end_sec: 3125.04
  text: 'these variational autoenccoders trained.

    How do you train these to generate How do you train these to generate How do you
    train these to generate

    images? Let''s say you give a sample of images? Let''s say you give a sample of
    images? Let''s say you give a sample of

    handwritten digits. How do you train a handwritten digits. How do you train a
    handwritten digits. How do you train a

    variation autoenccoders to generate variation autoenccoders to generate variation
    autoenccoders to generate

    these images? these images? these images?

    And this is very closely linked to the And this is very closely linked to the
    And this is very closely linked to the

    deep generative modeling lecture which deep generative modeling lecture which
    deep generative modeling lecture which

    was the first lecture where we said that was the first lecture where we said that
    was the first lecture where we said that

    the objective of all these deep the objective of all these deep the objective
    of all these deep

    generative models is to generative models is to generative models is to

    learn the underlying probability learn the underlying probability learn the underlying
    probability

    distribution and then sample from them. distribution and then sample from them.
    distribution and then sample from them.

    So this is exactly what the decoder So this is exactly what the decoder So this
    is exactly what the decoder

    does. The decoder is learning a does. The decoder is learning a does. The decoder
    is learning a

    distribution distribution distribution

    which is which is which is

    you know very close as possible to the you know very close as possible to the
    you know very close as possible to the

    true distribution which we don''t know true distribution which we don''t know
    true distribution which we don''t know

    but we only received the samples of data but we only received the samples of data
    but we only received the samples of data

    but from these samples of data we are but from these samples of data we are but
    from these samples of data we are

    trying to guess the true distribution trying to guess the true distribution trying
    to guess the true distribution

    and then sample from it. So we are going and then sample from it. So we are going'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 51
  start_sec: 3125.04
  end_sec: 3176.39
  text: 'and then sample from it. So we are going

    to take a real example in the next class to take a real example in the next class
    to take a real example in the next class

    where you will see exactly how deep where you will see exactly how deep where
    you will see exactly how deep

    generative model models work. How does generative model models work. How does
    generative model models work. How does

    the latin space distribution change over the latin space distribution change over
    the latin space distribution change over

    time and how are the images encoded in time and how are the images encoded in
    time and how are the images encoded in

    the latent space and how they are the latent space and how they are the latent
    space and how they are

    decoded back from the latin space. What decoded back from the latin space. What
    decoded back from the latin space. What

    are the architectures of the neural are the architectures of the neural are the
    architectures of the neural

    networks which are used within the networks which are used within the networks
    which are used within the

    encoder and within the decoder. So we encoder and within the decoder. So we encoder
    and within the decoder. So we

    will understand all of that. The main will understand all of that. The main will
    understand all of that. The main

    intuition for all of us to understand is intuition for all of us to understand
    is intuition for all of us to understand is

    that the Latin space is nothing but the that the Latin space is nothing but the
    that the Latin space is nothing but the

    hidden factors which capture the hidden factors which capture the hidden factors
    which capture the

    variations in the distribution. variations in the distribution. variations in
    the distribution.

    In the case of handwriting, it was the In the case of handwriting, it was the
    In the case of handwriting, it was the

    slant and the neatness. slant and the neatness. slant and the neatness.

    The variational part of the autoenccoder The variational part of the autoenccoder
    The variational part of the autoenccoder

    comes because the output of the encoder comes because the output of the encoder
    comes because the output of the encoder

    is not deterministic but rather it is'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 52
  start_sec: 3176.39
  end_sec: 3228.8
  text: 'is not deterministic but rather it is is not deterministic but rather it
    is

    probabilistic. probabilistic. probabilistic.

    And finally in your mind I want you to And finally in your mind I want you to
    And finally in your mind I want you to

    just close your eyes and imagine two just close your eyes and imagine two just
    close your eyes and imagine two

    machines. First machine takes the image machines. First machine takes the image
    machines. First machine takes the image

    input. Let''s say some student has input. Let''s say some student has input. Let''s
    say some student has

    written hello and it gives you four values. It gives you the mean of four values.
    It gives you the mean of

    the two levers and it gives you the the two levers and it gives you the the two
    levers and it gives you the

    deviation of the two livers. deviation of the two livers. deviation of the two
    livers.

    Now these four values you pass to the Now these four values you pass to the Now
    these four values you pass to the

    decoder which is another machine and you decoder which is another machine and
    you decoder which is another machine and you

    know which exactly which how how much to know which exactly which how how much
    to know which exactly which how how much to

    pull the levers. You pull the levers the pull the levers. You pull the levers
    the pull the levers. You pull the levers the

    decoder does its magic which is a decoder does its magic which is a decoder does
    its magic which is a

    trained neural network and you get the trained neural network and you get the
    trained neural network and you get the

    sample hello and you do this training so sample hello and you do this training
    so sample hello and you do this training so

    that the image which you have given at that the image which you have given at
    that the image which you have given at

    the start is as close as possible to the the start is as close as possible to
    the the start is as close as possible to the

    image which is generated at the end. image which is generated at the end.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 53
  start_sec: 3228.8
  end_sec: 3304.4
  text: 'image which is generated at the end.

    This is all that is happening in the This is all that is happening in the This
    is all that is happening in the

    variation autoenccoders. variation autoenccoders. variation autoenccoders.

    Thank you very much everyone and I''ll Thank you very much everyone and I''ll
    Thank you very much everyone and I''ll

    see you in the next lecture. Hello everyone and welcome to the third Hello everyone
    and welcome to the third

    lecture in the series principles of lecture in the series principles of lecture
    in the series principles of

    diffusion models. diffusion models.

    In [snorts] the first lecture we In [snorts] the first lecture we In [snorts]
    the first lecture we

    discussed about deep generative discussed about deep generative discussed about
    deep generative

    modeling. Then we discussed about modeling. Then we discussed about modeling.
    Then we discussed about

    principles of variational autoenccoders. principles of variational autoenccoders.
    principles of variational autoenccoders.

    And in today''s lecture, our main And in today''s lecture, our main And in today''s
    lecture, our main

    objective is to discuss training of objective is to discuss training of objective
    is to discuss training of

    variational autoenccoders. variational autoenccoders. variational autoenccoders.

    First of all, let us do a quick recap of First of all, let us do a quick recap
    of First of all, let us do a quick recap of

    what do we understand from variational what do we understand from variational
    what do we understand from variational

    autoenccoders up until this point. autoenccoders up until this point. autoenccoders
    up until this point.

    Let''s take a simple example of a Let''s take a simple example of a Let''s take
    a simple example of a

    handwriting handwriting handwriting

    which a student in your class has which a student in your class has which a student
    in your class has

    written. written. written.

    Let''s say they have written a number Let''s say they have written a number Let''s
    say they have written a number

    five. [snorts] You take that handwriting five. [snorts] You take that handwriting
    five. [snorts] You take that handwriting

    on a piece of paper on a piece of paper on a piece of paper

    and let''s say you have a machine which and let''s say you have a machine which
    and let''s say you have a machine which

    tells you the hidden factors of tells you the hidden factors of'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 54
  start_sec: 3304.4
  end_sec: 3370.069
  text: 'tells you the hidden factors of

    variation behind that image. variation behind that image. variation behind that
    image.

    [snorts] The machine tells you the hidden factors The machine tells you the hidden
    factors

    of variation behind that image. of variation behind that image. of variation behind
    that image.

    And the machine is very clever. It does And the machine is very clever. It does
    And the machine is very clever. It does

    not expect you to not expect you to not expect you to

    tell it how many hidden factors of tell it how many hidden factors of tell it
    how many hidden factors of

    variations are there or the meaning of variations are there or the meaning of
    variations are there or the meaning of

    those hidden factors but those hidden factors but those hidden factors but

    it it generates a mapping from the image it it generates a mapping from the image
    it it generates a mapping from the image

    to the hidden factors. An example of the to the hidden factors. An example of
    the to the hidden factors. An example of the

    hidden factors can be the slantness of hidden factors can be the slantness of
    hidden factors can be the slantness of

    the handwriting or the neatness of the the handwriting or the neatness of the
    the handwriting or the neatness of the

    handwriting. handwriting.

    Now another specialtity of that machine Now another specialtity of that machine
    Now another specialtity of that machine

    is that it does not just give you the is that it does not just give you the is
    that it does not just give you the

    numbers for the hidden factors but it numbers for the hidden factors but it numbers
    for the hidden factors but it

    gives you a distribution. It it says gives you a distribution. It it says gives
    you a distribution. It it says

    that your hidden factors is most that your hidden factors is most that your hidden
    factors is most

    probable to lie in this region. It gives probable to lie in this region. It gives
    probable to lie in this region. It gives

    you spaces in which the hidden factors you spaces in which the hidden factors
    you spaces in which the hidden factors

    can lie. So it appears to be a very'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 55
  start_sec: 3370.069
  end_sec: 3431.28
  text: 'can lie. So it appears to be a very can lie. So it appears to be a very

    smart and a clever machine. smart and a clever machine. smart and a clever machine.

    Okay. Now you have these hidden factors Okay. Now you have these hidden factors
    Okay. Now you have these hidden factors

    of variation. of variation. of variation.

    So you have captured something at the So you have captured something at the So
    you have captured something at the

    uh at the heart of the distribution. uh at the heart of the distribution. uh at
    the heart of the distribution.

    Really it''s it''s telling you which Really it''s it''s telling you which Really
    it''s it''s telling you which

    factors are most factors are most factors are most

    uh uh uh

    most are the most contributors to the most are the most contributors to the most
    are the most contributors to the

    variations in the distribution. variations in the distribution.

    Once you have these hidden factors, you Once you have these hidden factors, you
    Once you have these hidden factors, you

    have another machine which take these have another machine which take these have
    another machine which take these

    hidden factors as the input and hidden factors as the input and hidden factors
    as the input and

    you have levers which you can control. you have levers which you can control.
    you have levers which you can control.

    So you pull these levers. Let''s say you So you pull these levers. Let''s say
    you So you pull these levers. Let''s say you

    have two hidden factors. So you have two have two hidden factors. So you have
    two have two hidden factors. So you have two

    levers. You pull these levers levers. You pull these levers levers. You pull these
    levers

    corresponding to the hidden factor corresponding to the hidden factor corresponding
    to the hidden factor

    spaces spaces spaces

    and then you finally get an image at the and then you finally get an image at
    the and then you finally get an image at the

    end. end. end.

    Now the main objective of this Now the main objective of this Now the main objective
    of this

    variational autoenccoder setup is that variational autoenccoder setup is that
    variational autoenccoder setup is that

    the final image should be as close as the final image should be as close as'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 56
  start_sec: 3431.28
  end_sec: 3490.24
  text: 'the final image should be as close as

    possible to the original image. So you possible to the original image. So you
    possible to the original image. So you

    can see that there has to be some kind can see that there has to be some kind
    can see that there has to be some kind

    of training objective in this whole of training objective in this whole of training
    objective in this whole

    setup. setup. setup.

    The first image that we discussed is The first image that we discussed is The
    first image that we discussed is

    called as the encoder and the second called as the encoder and the second called
    as the encoder and the second

    image that we discussed is called as the image that we discussed is called as
    the image that we discussed is called as the

    decoder. decoder.

    And this entire pipeline is called as And this entire pipeline is called as And
    this entire pipeline is called as

    variational autoenccoder pipeline. variational autoenccoder pipeline. variational
    autoenccoder pipeline.

    Now what we are going to understand is Now what we are going to understand is
    Now what we are going to understand is

    how do we train this variational how do we train this variational how do we train
    this variational

    autoenccoder pipeline so that the final autoenccoder pipeline so that the final
    autoenccoder pipeline so that the final

    image which is also called as the image which is also called as the image which
    is also called as the

    reconstructed image is as close as reconstructed image is as close as reconstructed
    image is as close as

    possible to the original image. possible to the original image. possible to the
    original image.

    Now the first observation that we can Now the first observation that we can Now
    the first observation that we can

    make is there are two neural networks make is there are two neural networks make
    is there are two neural networks

    here. This is the first neural network here. This is the first neural network
    here. This is the first neural network

    which is the machine which learns to which is the machine which learns to which
    is the machine which learns to

    encode and the second neural network is encode and the second neural network is'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 57
  start_sec: 3490.24
  end_sec: 3560.549
  text: 'encode and the second neural network is

    the machine which learns to decode. the machine which learns to decode. the machine
    which learns to decode.

    So somehow we have to train the So somehow we have to train the So somehow we
    have to train the

    parameters of these neural networks parameters of these neural networks parameters
    of these neural networks

    to optimize something. The question is to optimize something. The question is
    to optimize something. The question is

    what is the objective function that we what is the objective function that we
    what is the objective function that we

    want to optimize in this scenario? want to optimize in this scenario? want to
    optimize in this scenario?

    Let us think from the first principles. Let us think from the first principles.
    Let us think from the first principles.

    We started off with the objective that We started off with the objective that
    We started off with the objective that

    we want our probability distribution to we want our probability distribution to
    we want our probability distribution to

    match the true probability distribution match the true probability distribution
    match the true probability distribution

    of the underlying data. Right? So this of the underlying data. Right? So this
    of the underlying data. Right? So this

    distribution should match this distribution should match this distribution should
    match this

    distribution as close as possible. distribution as close as possible. distribution
    as close as possible.

    That means that we want to maximize the That means that we want to maximize the
    That means that we want to maximize the

    following. So this means that So this means that

    if you give an input image if you give an input image if you give an input image

    then the decoder network should give a then the decoder network should give a
    then the decoder network should give a

    probability which is very high right probability which is very high right probability
    which is very high right

    this means that I''ve trained my this means that I''ve trained my this means that
    I''ve trained my

    variational autoenccoder pro properly variational autoenccoder pro properly variational
    autoenccoder pro properly

    for example let''s say the input image is for example let''s say the input image
    is for example let''s say the input image is

    a dot like this and you pass it to the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 58
  start_sec: 3560.549
  end_sec: 3607.28
  text: 'a dot like this and you pass it to the a dot like this and you pass it to
    the

    decoder and you get a value of zero decoder and you get a value of zero decoder
    and you get a value of zero

    which which means that your decoder is which which means that your decoder is
    which which means that your decoder is

    saying that this image is not likely to saying that this image is not likely to
    saying that this image is not likely to

    be found in your distribution which is be found in your distribution which is
    be found in your distribution which is

    not true right because I have taken the not true right because I have taken the
    not true right because I have taken the

    image from the distribution itself so image from the distribution itself so image
    from the distribution itself so

    this should be assigned a very high this should be assigned a very high this should
    be assigned a very high

    value like 0.9 or something like that value like 0.9 or something like that value
    like 0.9 or something like that

    so I want to maximize the following I so I want to maximize the following I so
    I want to maximize the following I

    want to maximize the probability of want to maximize the probability of want to
    maximize the probability of

    drawing the real samples from the drawing the real samples from the drawing the
    real samples from the

    predicted distribution predicted distribution predicted distribution

    this means that we have done a good job this means that we have done a good job
    this means that we have done a good job

    in modeling our true distribution. in modeling our true distribution. in modeling
    our true distribution.

    You can see that we are consistent with You can see that we are consistent with
    You can see that we are consistent with

    our notations here. In the first lecture our notations here. In the first lecture
    our notations here. In the first lecture

    also we use this notation of P5 of X for also we use this notation of P5 of X
    for also we use this notation of P5 of X for

    our predicted distribution which should our predicted distribution which should'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 59
  start_sec: 3607.28
  end_sec: 3679.839
  text: 'our predicted distribution which should

    match as close as possible to the true match as close as possible to the true
    match as close as possible to the true

    distribution which we do not really distribution which we do not really distribution
    which we do not really

    know. know. know.

    Now the problem is that calculating this Now the problem is that calculating this
    Now the problem is that calculating this

    probability is not straightforward. Why it is not straightforward? Why it is not
    straightforward?

    Let''s take an example of Let''s take an example of Let''s take an example of

    uh the digit five. The question we are uh the digit five. The question we are
    uh the digit five. The question we are

    asking is what is the probability of asking is what is the probability of asking
    is what is the probability of

    finding the digit five from our decoder finding the digit five from our decoder
    finding the digit five from our decoder

    distribution? distribution? distribution?

    How do we calculate the above How do we calculate the above How do we calculate
    the above

    probability? probability? probability?

    uh we first uh we first uh we first

    look at the latent space look at the latent space look at the latent space

    and and

    we say that okay now first take this we say that okay now first take this we say
    that okay now first take this

    point and generate a digit five from it point and generate a digit five from it
    point and generate a digit five from it

    calculate the probability of that then calculate the probability of that then
    calculate the probability of that then

    we''ll take this point generate digit we''ll take this point generate digit we''ll
    take this point generate digit

    five calculate the probability of that five calculate the probability of that
    five calculate the probability of that

    then we''ll take this point calculate the then we''ll take this point calculate
    the then we''ll take this point calculate the

    probability of that so essentially we probability of that so essentially we probability
    of that so essentially we

    are integrating over all the possible are integrating over all the possible are
    integrating over all the possible

    points in the latin space which is also points in the latin space which is also'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 60
  start_sec: 3679.839
  end_sec: 3741.04
  text: 'points in the latin space which is also

    given in this formula. given in this formula. given in this formula.

    I I don''t want to stress too much on how I I don''t want to stress too much on
    how I I don''t want to stress too much on how

    this formula is really appearing but this formula is really appearing but this
    formula is really appearing but

    it''s basically saying that probability it''s basically saying that probability
    it''s basically saying that probability

    of of

    uh image X from the predicted uh image X from the predicted uh image X from the
    predicted

    distribution is given by a summation of distribution is given by a summation of
    distribution is given by a summation of

    probability probability probability

    from the decoder distribution multiplied from the decoder distribution multiplied
    from the decoder distribution multiplied

    by the probability of the latent space by the probability of the latent space
    by the probability of the latent space

    probability of the variable in the probability of the variable in the probability
    of the variable in the

    latent space which corresponds to that latent space which corresponds to that
    latent space which corresponds to that

    image. So for example, this variation image. So for example, this variation image.
    So for example, this variation

    variable in the Latin space can be variable in the Latin space can be variable
    in the Latin space can be

    anything. We take all these variables, anything. We take all these variables,
    anything. We take all these variables,

    we find the probability of that we find the probability of that we find the probability
    of that

    variable, we pass it to the decoded and variable, we pass it to the decoded and
    variable, we pass it to the decoded and

    then find the probability from the then find the probability from the then find
    the probability from the

    decoder distribution and then sum decoder distribution and then sum decoder distribution
    and then sum

    everything up. everything up. everything up.

    If you remember, we have looked a same If you remember, we have looked a same
    If you remember, we have looked a same

    we have looked at the same analogy in uh we have looked at the same analogy in
    uh we have looked at the same analogy in uh

    the visualization before where we saw the visualization before where we saw'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 61
  start_sec: 3741.04
  end_sec: 3797.44
  text: 'the visualization before where we saw

    that it''s like finding or that it''s like finding or that it''s like finding
    or

    sampling for from a very giant ocean and sampling for from a very giant ocean
    and sampling for from a very giant ocean and

    this is this is not very tractable. this is this is not very tractable. this is
    this is not very tractable.

    So this is something which people were So this is something which people were
    So this is something which people were

    stuck at. They were trying to think okay stuck at. They were trying to think okay
    stuck at. They were trying to think okay

    I want to maximize this objective I want to maximize this objective I want to
    maximize this objective

    function but to maximize the objective function but to maximize the objective
    function but to maximize the objective

    function I need to sample from function I need to sample from function I need
    to sample from

    everywhere in the latin space everywhere in the latin space everywhere in the
    latin space

    and I am not sure how do we do that and I am not sure how do we do that and I
    am not sure how do we do that

    because then the integral will become because then the integral will become because
    then the integral will become

    intractable. It essentially means that intractable. It essentially means that
    intractable. It essentially means that

    we look at all possible variations in we look at all possible variations in we
    look at all possible variations in

    the hidden factors and sum over all the the hidden factors and sum over all the
    the hidden factors and sum over all the

    probabilities over all these hidden probabilities over all these hidden probabilities
    over all these hidden

    factors factors factors

    and hence this is mathematically and hence this is mathematically and hence this
    is mathematically

    intractable. intractable. intractable.

    How can we go over every single point in How can we go over every single point
    in How can we go over every single point in

    the latent space and find out the the latent space and find out the the latent
    space and find out the

    probability of the sample drawn from probability of the sample drawn from probability
    of the sample drawn from

    that point being real? that point being real?'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 62
  start_sec: 3797.44
  end_sec: 3866.95
  text: 'that point being real?

    And this actually does not even make use And this actually does not even make
    use And this actually does not even make use

    of the encoder. This is all decoder of the encoder. This is all decoder of the
    encoder. This is all decoder

    based. You can see there is no Q theta based. You can see there is no Q theta
    based. You can see there is no Q theta

    over here. It''s everything is decoder over here. It''s everything is decoder
    over here. It''s everything is decoder

    based. [snorts] based. [snorts] based. [snorts]

    So this is something which is highly So this is something which is highly So this
    is something which is highly

    intractable. intractable.

    U since we are not making use of our U since we are not making use of our U since
    we are not making use of our

    semantic dis or semantic division of the semantic dis or semantic division of
    the semantic dis or semantic division of the

    latent space which our encoder is latent space which our encoder is latent space
    which our encoder is

    already doing. So you don''t really need already doing. So you don''t really need
    already doing. So you don''t really need

    to sample from everything. Right? to sample from everything. Right? to sample
    from everything. Right?

    [snorts] [snorts]

    Okay. So we need a computable training Okay. So we need a computable training
    Okay. So we need a computable training

    objective. We need something which we objective. We need something which we objective.
    We need something which we

    can mathematically compute can mathematically compute can mathematically compute

    and this is where training via the and this is where training via the and this
    is where training via the

    evidence lower bound which is also evidence lower bound which is also evidence
    lower bound which is also

    called as the elbow comes in the called as the elbow comes in the called as the
    elbow comes in the

    picture. So in variation autoenccoders what we do So in variation autoenccoders
    what we do

    is that we do not maximize this is that we do not maximize this is that we do
    not maximize this

    objective but we maximize the elbow objective but we maximize the elbow objective
    but we maximize the elbow

    objective. objective. objective.

    Now the question is that what is the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 63
  start_sec: 3866.95
  end_sec: 3925.28
  text: 'Now the question is that what is the Now the question is that what is the

    elbow objective? [snorts] elbow objective? [snorts] elbow objective? [snorts]

    Well to understand this let''s understand Well to understand this let''s understand
    Well to understand this let''s understand

    something very simple to begin with. Let something very simple to begin with.
    Let something very simple to begin with. Let

    us say we have this true objective us say we have this true objective us say we
    have this true objective

    function which we want to optimize and function which we want to optimize and
    function which we want to optimize and

    we have another function which is always we have another function which is always
    we have another function which is always

    less than the true objective function less than the true objective function less
    than the true objective function

    which means that which means that which means that

    if we maximize this if we maximize this if we maximize this

    then the green line will always be above then the green line will always be above
    then the green line will always be above

    the red line. So that will anyways be the red line. So that will anyways be the
    red line. So that will anyways be

    maximized. maximized. maximized.

    So then people say that instead of So then people say that instead of So then
    people say that instead of

    maximizing the green line which we don''t maximizing the green line which we don''t
    maximizing the green line which we don''t

    know how to compute, we maximize the red know how to compute, we maximize the
    red know how to compute, we maximize the red

    line which we know is always going to line which we know is always going to line
    which we know is always going to

    lie below the green line lie below the green line lie below the green line

    which is the elbow objective. which is the elbow objective. which is the elbow
    objective.

    So uh the elbow which is the evidence So uh the elbow which is the evidence So
    uh the elbow which is the evidence

    lower bound is divided into two terms. lower bound is divided into two terms.
    lower bound is divided into two terms.

    I will not get very mathematical here I will not get very mathematical here'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 64
  start_sec: 3925.28
  end_sec: 3984.48
  text: 'I will not get very mathematical here

    and I will not focus too much on the and I will not focus too much on the and
    I will not focus too much on the

    derivation but I will provide a link in derivation but I will provide a link in
    derivation but I will provide a link in

    the the

    uh description which goes over the uh description which goes over the uh description
    which goes over the

    entire derivation. It''s it''s not very entire derivation. It''s it''s not very
    entire derivation. It''s it''s not very

    difficult to understand but right now I difficult to understand but right now
    I difficult to understand but right now I

    want to provide an intuition for you want to provide an intuition for you want
    to provide an intuition for you

    which can help you in your practical which can help you in your practical which
    can help you in your practical

    projects. So the evidence lower bound is projects. So the evidence lower bound
    is projects. So the evidence lower bound is

    made up of two terms which are given made up of two terms which are given made
    up of two terms which are given

    below. below. below.

    the the first term is the reconstruction the the first term is the reconstruction
    the the first term is the reconstruction

    term which is the probability of from term which is the probability of from term
    which is the probability of from

    the decoder. the decoder. the decoder.

    Uh this term essentially says that the Uh this term essentially says that the
    Uh this term essentially says that the

    reconstructed output is similar to the reconstructed output is similar to the
    reconstructed output is similar to the

    original input. So we are trying to original input. So we are trying to original
    input. So we are trying to

    maximize this term which means that the maximize this term which means that the
    maximize this term which means that the

    probability of sampling the image from probability of sampling the image from
    probability of sampling the image from

    the decoder distribution given the the decoder distribution given the the decoder
    distribution given the

    latent variable which is generating that latent variable which is generating that
    latent variable which is generating that

    image. image. image.

    So this essentially says that So this essentially says that'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 65
  start_sec: 3984.48
  end_sec: 4053.52
  text: 'So this essentially says that

    whatever image you''re looking at the end whatever image you''re looking at the
    end whatever image you''re looking at the end

    is that image is that image is that image

    uh as close is is the reconstructed uh as close is is the reconstructed uh as
    close is is the reconstructed

    output similar to the original input. output similar to the original input. output
    similar to the original input.

    This is what uh the reconstruction term This is what uh the reconstruction term
    This is what uh the reconstruction term

    is trying to say. is trying to say. is trying to say.

    The second term which is not very The second term which is not very The second
    term which is not very

    straightforward is called as the straightforward is called as the straightforward
    is called as the

    regularization term. regularization term. regularization term.

    and it essentially and it essentially and it essentially

    encourages the encoder distribution to encourages the encoder distribution to
    encourages the encoder distribution to

    stay as close as possible to the assumed stay as close as possible to the assumed
    stay as close as possible to the assumed

    distribution of the latent variables distribution of the latent variables distribution
    of the latent variables

    which is quite commonly a gshian which is quite commonly a gshian which is quite
    commonly a gshian

    distribution. distribution. distribution.

    So what that means is that if you look So what that means is that if you look
    So what that means is that if you look

    at the first at the first at the first

    discussion about the latent space we had discussion about the latent space we
    had discussion about the latent space we had

    here we had initiated our discussion here we had initiated our discussion here
    we had initiated our discussion

    that the latent space that the latent space that the latent space

    the variables or uh the data samples in the variables or uh the data samples in
    the variables or uh the data samples in

    the real space when we transform that to the real space when we transform that
    to the real space when we transform that to

    the latent space they can be distributed the latent space they can be distributed
    the latent space they can be distributed

    in any fashion but in any fashion but'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 66
  start_sec: 4053.52
  end_sec: 4110.07
  text: 'in any fashion but

    in more realistic settings the in more realistic settings the in more realistic
    settings the

    distribution is more likely to be distribution is more likely to be distribution
    is more likely to be

    washian because there is going to be an washian because there is going to be an
    washian because there is going to be an

    average value and the extremes are going average value and the extremes are going
    average value and the extremes are going

    to have very low probabilities to have very low probabilities to have very low
    probabilities

    which is something which you see in this which is something which you see in this
    which is something which you see in this

    distribution also. So we want the distribution also. So we want the distribution
    also. So we want the

    distribution in the latent space which distribution in the latent space which
    distribution in the latent space which

    is generated by the encoder which is the is generated by the encoder which is
    the is generated by the encoder which is the

    first machine first machine first machine

    to be as close as possible to a gshian to be as close as possible to a gshian
    to be as close as possible to a gshian

    distribution which is distribution which is distribution which is

    centered around the mean with a fixed centered around the mean with a fixed centered
    around the mean with a fixed

    variance. variance. variance.

    And my intuition behind this is that And my intuition behind this is that And
    my intuition behind this is that

    most of the real life processes can be most of the real life processes can be
    most of the real life processes can be

    modeled as goshian. For example, modeled as goshian. For example, modeled as goshian.
    For example,

    distribution of handwriting. distribution of handwriting. distribution of handwriting.

    Let''s take an example of that. Let''s take an example of that. Let''s take an
    example of that.

    There will be few people with very very There will be few people with very very
    There will be few people with very very

    good handwriting and very very bad good handwriting and very very bad good handwriting
    and very very bad

    handwriting. But most of the handwriting handwriting. But most of the handwriting
    handwriting. But most of the handwriting

    will be average in terms of the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 67
  start_sec: 4110.07
  end_sec: 4172.719
  text: 'will be average in terms of the will be average in terms of the

    slantness, in terms of the neatness etc. slantness, in terms of the neatness etc.
    slantness, in terms of the neatness etc.

    So we are So we are So we are

    thinking something from a pure human thinking something from a pure human thinking
    something from a pure human

    intuition point of view and we are intuition point of view and we are intuition
    point of view and we are

    bringing that into the objective bringing that into the objective bringing that
    into the objective

    function function function

    where we are saying that the divergence where we are saying that the divergence
    where we are saying that the divergence

    between between between

    [snorts] the encoder distribution and [snorts] the encoder distribution and [snorts]
    the encoder distribution and

    the latin distribution which is quite the latin distribution which is quite the
    latin distribution which is quite

    commonly a goshian commonly a goshian commonly a goshian

    has to be minimized. has to be minimized. has to be minimized.

    We have looked at this symbol before. We have looked at this symbol before. We
    have looked at this symbol before.

    This is the kale divergence. It means This is the kale divergence. It means This
    is the kale divergence. It means

    that that that

    it means or it symbolizes or signifies it means or it symbolizes or signifies
    it means or it symbolizes or signifies

    the distance between the two probability the distance between the two probability
    the distance between the two probability

    distributions. So essentially we want to distributions. So essentially we want
    to distributions. So essentially we want to

    minimize this. So we want to maximize minimize this. So we want to maximize minimize
    this. So we want to maximize

    the negative of this. So when you add the negative of this. So when you add the
    negative of this. So when you add

    term one and term two you get the elbow term one and term two you get the elbow
    term one and term two you get the elbow

    objective which says log of probability objective which says log of probability
    objective which says log of probability

    of x given zed which means that of x given zed which means that of x given zed
    which means that

    how likely is the reconstructed how likely is the reconstructed'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 68
  start_sec: 4172.719
  end_sec: 4235.199
  text: 'how likely is the reconstructed

    um output. um output. um output.

    What is the probability of that? And we What is the probability of that? And we
    What is the probability of that? And we

    want to maximize this because it means want to maximize this because it means
    want to maximize this because it means

    that our that our that our

    original distribution original distribution original distribution

    is as close as possible to the is as close as possible to the is as close as possible
    to the

    distribution that we are trying to distribution that we are trying to distribution
    that we are trying to

    predict. predict. predict.

    You can see that we wanted to maximize You can see that we wanted to maximize
    You can see that we wanted to maximize

    this actually but we have this actually but we have this actually but we have

    changed it to x given z which is given changed it to x given z which is given
    changed it to x given z which is given

    the latent space uh given the sample the latent space uh given the sample the
    latent space uh given the sample

    from the latent space. What is the from the latent space. What is the from the
    latent space. What is the

    probability of the image which is probability of the image which is probability
    of the image which is

    generated from that sample? And if this generated from that sample? And if this
    generated from that sample? And if this

    is very high, it means that is very high, it means that is very high, it means
    that

    our decoder distribution is our decoder distribution is our decoder distribution
    is

    assigning higher probabilities to assigning higher probabilities to assigning
    higher probabilities to

    samples which are already there in the samples which are already there in the
    samples which are already there in the

    data which is exactly what we want. data which is exactly what we want. data which
    is exactly what we want.

    And this is something which is uh added And this is something which is uh added
    And this is something which is uh added

    as an additional term because we want as an additional term because we want as
    an additional term because we want

    our encoder distribution to stay as our encoder distribution to stay as'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 69
  start_sec: 4235.199
  end_sec: 4298.32
  text: 'our encoder distribution to stay as

    close as possible to a gshian which close as possible to a gshian which close
    as possible to a gshian which

    comes from our human intuition that comes from our human intuition that comes
    from our human intuition that

    every the hidden factors which every the hidden factors which every the hidden
    factors which

    you know dictate anything any process you know dictate anything any process you
    know dictate anything any process

    has to be a gshian which is an has to be a gshian which is an has to be a gshian
    which is an

    assumption at the end of it. assumption at the end of it. assumption at the end
    of it.

    Now we will look at a visual explanation Now we will look at a visual explanation
    Now we will look at a visual explanation

    of this so that you understand how does of this so that you understand how does
    of this so that you understand how does

    the elbow objective look like and you the elbow objective look like and you the
    elbow objective look like and you

    have a visual intuition in your mind. Okay, let me start from the first. Okay,
    let me start from the first.

    Okay, so we are going to take a very Okay, so we are going to take a very Okay,
    so we are going to take a very

    interesting example. Imagine we want to interesting example. Imagine we want to
    interesting example. Imagine we want to

    teleport a cat from Earth to Mars. teleport a cat from Earth to Mars. teleport
    a cat from Earth to Mars.

    Okay. So, uh we have an earth cat and we Okay. So, uh we have an earth cat and
    we Okay. So, uh we have an earth cat and we

    want to take this same cat to the Mars. want to take this same cat to the Mars.
    want to take this same cat to the Mars.

    Now, sending every single atom is not Now, sending every single atom is not Now,
    sending every single atom is not

    possible. It''s too much data. So, we possible. It''s too much data. So, we possible.
    It''s too much data. So, we

    want to compress the earth cat into want to compress the earth cat into'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 70
  start_sec: 4298.32
  end_sec: 4350.48
  text: 'want to compress the earth cat into

    something which captures the essence of something which captures the essence of
    something which captures the essence of

    the cat. We want to send a secret recipe the cat. We want to send a secret recipe
    the cat. We want to send a secret recipe

    or the Latin code which is the which is or the Latin code which is the which is
    or the Latin code which is the which is

    called as zed. So the Latin code encodes called as zed. So the Latin code encodes
    called as zed. So the Latin code encodes

    the hidden factors of variation and then the hidden factors of variation and then
    the hidden factors of variation and then

    you can decode it in Mars and generate you can decode it in Mars and generate
    you can decode it in Mars and generate

    the cat. the cat. the cat.

    Now we want to maximize the probability Now we want to maximize the probability
    Now we want to maximize the probability

    of the cats which are generated by our of the cats which are generated by our
    of the cats which are generated by our

    decoder decoder decoder

    which which lie in the original which which lie in the original which which lie
    in the original

    distribution. So this is the true distribution. So this is the true distribution.
    So this is the true

    objective function which we want to objective function which we want to objective
    function which we want to

    maximize and it involves an infinite maximize and it involves an infinite maximize
    and it involves an infinite

    integral. It''s very difficult but we we integral. It''s very difficult but we
    we integral. It''s very difficult but we we

    can calculate the evidence lower bound. can calculate the evidence lower bound.
    can calculate the evidence lower bound.

    So what we do is that we calculate the So what we do is that we calculate the
    So what we do is that we calculate the

    evidence or uh the evidence lower bound evidence or uh the evidence lower bound
    evidence or uh the evidence lower bound

    which is always less than the true which is always less than the true which is
    always less than the true

    objective and we try to maximize the objective and we try to maximize the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 71
  start_sec: 4350.48
  end_sec: 4407.36
  text: 'objective and we try to maximize the

    elbow. elbow. elbow.

    So since the true objective is always So since the true objective is always So
    since the true objective is always

    greater than the elbow, maximizing the greater than the elbow, maximizing the
    greater than the elbow, maximizing the

    elbow is going to maximize the true elbow is going to maximize the true elbow
    is going to maximize the true

    objective also. Now how do we maximize objective also. Now how do we maximize
    objective also. Now how do we maximize

    the elbow? By balancing two goals. The the elbow? By balancing two goals. The
    the elbow? By balancing two goals. The

    first goal first goal first goal

    is also called as the reconstruction is also called as the reconstruction is also
    called as the reconstruction

    accuracy. Which means that does the cat accuracy. Which means that does the cat
    accuracy. Which means that does the cat

    which is generated in the marks Mars which is generated in the marks Mars which
    is generated in the marks Mars

    look all right? Does it look close to look all right? Does it look close to look
    all right? Does it look close to

    the real earth cat? So we want a maximum the real earth cat? So we want a maximum
    the real earth cat? So we want a maximum

    similarity between these two. And the similarity between these two. And the similarity
    between these two. And the

    second is the regularization term which second is the regularization term which
    second is the regularization term which

    means that [snorts] is the recipe means that [snorts] is the recipe means that
    [snorts] is the recipe

    given in a standard language. Does the given in a standard language. Does the
    given in a standard language. Does the

    recipe make sense? So if our recipe is recipe make sense? So if our recipe is
    recipe make sense? So if our recipe is

    initially purple and the standard prior initially purple and the standard prior
    initially purple and the standard prior

    which is the gshian is in yellow, we which is the gshian is in yellow, we which
    is the gshian is in yellow, we

    want to move our code to the yellow want to move our code to the yellow'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 72
  start_sec: 4407.36
  end_sec: 4463.669
  text: 'want to move our code to the yellow

    distribution. We want to move it as distribution. We want to move it as distribution.
    We want to move it as

    close as possible to the normal close as possible to the normal close as possible
    to the normal

    distribution. distribution.

    This is exactly what the elbow training This is exactly what the elbow training
    This is exactly what the elbow training

    objective does. So by maximizing elbow objective does. So by maximizing elbow
    objective does. So by maximizing elbow

    we get accurate reconstructions and we get accurate reconstructions and we get
    accurate reconstructions and

    organized distribution in the latent organized distribution in the latent organized
    distribution in the latent

    space which makes sense. So you can again go through this So you can again go
    through this

    animation uh if you want some parts of animation uh if you want some parts of
    animation uh if you want some parts of

    it to be cleared. [snorts] it to be cleared. [snorts] it to be cleared. [snorts]

    But to train the variation But to train the variation But to train the variation

    autoenccoders, we want to maximize our autoenccoders, we want to maximize our
    autoenccoders, we want to maximize our

    elbow. And this brings in not just the elbow. And this brings in not just the
    elbow. And this brings in not just the

    decoder but it brings in the encoder decoder but it brings in the encoder decoder
    but it brings in the encoder

    also. So essentially we are we are max also. So essentially we are we are max
    also. So essentially we are we are max

    we are training the weights of two we are training the weights of two we are training
    the weights of two

    neural networks to maximize the elbow. neural networks to maximize the elbow.
    neural networks to maximize the elbow.

    It''s quite interesting in a way that uh It''s quite interesting in a way that
    uh It''s quite interesting in a way that uh

    you know it once you go through the you know it once you go through the you know
    it once you go through the

    mathematics at the end of it this is mathematics at the end of it this is mathematics
    at the end of it this is

    what remains and it makes sense from an'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 73
  start_sec: 4463.669
  end_sec: 4520.96
  text: 'what remains and it makes sense from an what remains and it makes sense from
    an

    intuitive standpoint because later intuitive standpoint because later intuitive
    standpoint because later

    people forget the mathematics but they people forget the mathematics but they
    people forget the mathematics but they

    do remember this intuition do remember this intuition do remember this intuition

    and the reconstruction term makes sense. and the reconstruction term makes sense.
    and the reconstruction term makes sense.

    The regularization term is something The regularization term is something The
    regularization term is something

    which makes the VA special because it which makes the VA special because it which
    makes the VA special because it

    essentially means that you''re imposing essentially means that you''re imposing
    essentially means that you''re imposing

    some constraint on your latent space some constraint on your latent space some
    constraint on your latent space

    distribution which is not really there distribution which is not really there
    distribution which is not really there

    in an autoenccoder it in a in a plain in an autoenccoder it in a in a plain in
    an autoenccoder it in a in a plain

    autoenccoder. So here we have a autoenccoder. So here we have a autoenccoder.
    So here we have a

    reconstruction term and we have a reconstruction term and we have a reconstruction
    term and we have a

    regularization term as well. Okay. [snorts] So now in the last part Okay. [snorts]
    So now in the last part

    of this lecture we are going to take a of this lecture we are going to take a
    of this lecture we are going to take a

    practical example which is going to help practical example which is going to help
    practical example which is going to help

    us understand us understand us understand

    how the elbow method is used to train a how the elbow method is used to train
    a how the elbow method is used to train a

    variational autoenccoder. variational autoenccoder.

    So everything that we have looked at so So everything that we have looked at so
    So everything that we have looked at so

    far in this in these two lectures is far in this in these two lectures is far
    in this in these two lectures is

    going to come together very nicely in going to come together very nicely in'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 74
  start_sec: 4520.96
  end_sec: 4581.35
  text: 'going to come together very nicely in

    this last practical example. Our task is this last practical example. Our task
    is this last practical example. Our task is

    to train a variation autoenccoder to to train a variation autoenccoder to to train
    a variation autoenccoder to

    predict the true distribution that predict the true distribution that predict
    the true distribution that

    generates emnest handwritten digits and generates emnest handwritten digits and
    generates emnest handwritten digits and

    we want to generate samples from that we want to generate samples from that we
    want to generate samples from that

    predicted distribution. So this this very closely aligns to the So this this very
    closely aligns to the

    deep generative modeling task because deep generative modeling task because deep
    generative modeling task because

    there is a two distribution which we do there is a two distribution which we do
    there is a two distribution which we do

    not know. we only have the samples of not know. we only have the samples of not
    know. we only have the samples of

    data and from that samples of data we data and from that samples of data we data
    and from that samples of data we

    want to learn the true distribution. want to learn the true distribution. want
    to learn the true distribution.

    Okay. So let''s see now we have this Okay. So let''s see now we have this Okay.
    So let''s see now we have this

    information we have all these images information we have all these images information
    we have all these images

    which are coming to us and which are coming to us and which are coming to us and

    first let''s think of the second machine first let''s think of the second machine
    first let''s think of the second machine

    the machine which which is going to take the machine which which is going to take
    the machine which which is going to take

    the latent variables as the input and the latent variables as the input and the
    latent variables as the input and

    it''s going to generate the output. So it''s going to generate the output. So
    it''s going to generate the output. So

    here we will assume that there are two here we will assume that there are two
    here we will assume that there are two

    hidden factors which we have absolutely'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 75
  start_sec: 4581.35
  end_sec: 4633.04
  text: 'hidden factors which we have absolutely hidden factors which we have absolutely

    no clue what they are but the encoder is no clue what they are but the encoder
    is no clue what they are but the encoder is

    going to find that out for us but let''s going to find that out for us but let''s
    going to find that out for us but let''s

    assume that there are two hidden factors assume that there are two hidden factors
    assume that there are two hidden factors

    which govern the variation of these which govern the variation of these which
    govern the variation of these

    digits which itself is digits which itself is digits which itself is

    very interesting right how can two very interesting right how can two very interesting
    right how can two

    factors govern the distribution of factors govern the distribution of factors
    govern the distribution of

    everything everything everything

    I think this is where neural networks I think this is where neural networks I
    think this is where neural networks

    really excel humans can''t really really excel humans can''t really really excel
    humans can''t really

    understand what these factors are. In my understand what these factors are. In
    my understand what these factors are. In my

    mind, I can only think of neatness, mind, I can only think of neatness, mind,
    I can only think of neatness,

    slantness, how much pressure you apply slantness, how much pressure you apply
    slantness, how much pressure you apply

    etc. But there might be something which etc. But there might be something which
    etc. But there might be something which

    we cannot put in words which the neural we cannot put in words which the neural
    we cannot put in words which the neural

    network captures. network captures. network captures.

    Okay. So the decoder has to take these Okay. So the decoder has to take these
    Okay. So the decoder has to take these

    two values and it has to predict the two values and it has to predict the two
    values and it has to predict the

    image. So there has to be some neural image. So there has to be some neural image.
    So there has to be some neural

    network structure in between. network structure in between. network structure
    in between.

    So remember our decoder setup looks like So remember our decoder setup looks like'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 76
  start_sec: 4633.04
  end_sec: 4690.87
  text: 'So remember our decoder setup looks like

    this. It''s it it needs to take the this. It''s it it needs to take the this.
    It''s it it needs to take the

    sample from the latent space and then it sample from the latent space and then
    it sample from the latent space and then it

    needs to generate an image. So it''s it''s a distribution which maps So it''s
    it''s a distribution which maps

    from the latent space to the input image from the latent space to the input image
    from the latent space to the input image

    space. space. space.

    Okay. So uh for every single pixel Okay. So uh for every single pixel Okay. So
    uh for every single pixel

    we need a value. we need a value. we need a value.

    So this three for example it it can be So this three for example it it can be
    So this three for example it it can be

    divided as 28 by 28. So there are 784 divided as 28 by 28. So there are 784 divided
    as 28 by 28. So there are 784

    pixels pixels

    and if we go for a deterministic and if we go for a deterministic and if we go
    for a deterministic

    approach we only need the mean which approach we only need the mean which approach
    we only need the mean which

    which are 784. If we go for a which are 784. If we go for a which are 784. If
    we go for a

    probabilistic approach we need 784 into probabilistic approach we need 784 into
    probabilistic approach we need 784 into

    two values. Here we will go with a two values. Here we will go with a two values.
    Here we will go with a

    deterministic approach. So our neural deterministic approach. So our neural deterministic
    approach. So our neural

    network will take two values as the network will take two values as the network
    will take two values as the

    input and it will predict 784 values as input and it will predict 784 values as
    input and it will predict 784 values as

    the output which are the mean for all the output which are the mean for all the
    output which are the mean for all

    these pixels. these pixels. these pixels.

    So it should take the latent vector and'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 77
  start_sec: 4690.87
  end_sec: 4747.92
  text: 'So it should take the latent vector and So it should take the latent vector
    and

    it should generate the reconstructed it should generate the reconstructed it should
    generate the reconstructed

    image. Right? image. Right? image. Right?

    So this is how the neural the the So this is how the neural the the So this is
    how the neural the the

    decoder network architecture looks like. decoder network architecture looks like.
    decoder network architecture looks like.

    It takes two images. Uh it it takes two It takes two images. Uh it it takes two
    It takes two images. Uh it it takes two

    variables as an input which is the variables as an input which is the variables
    as an input which is the

    latent space. Then there is a hidden latent space. Then there is a hidden latent
    space. Then there is a hidden

    layer with 400 neurons. So two neurons layer with 400 neurons. So two neurons
    layer with 400 neurons. So two neurons

    as an input. Hidden layer with 400 as an input. Hidden layer with 400 as an input.
    Hidden layer with 400

    neurons. And the final layer has 784 neurons. And the final layer has 784 neurons.
    And the final layer has 784

    neurons which are the values of the mean neurons which are the values of the mean
    neurons which are the values of the mean

    of all these pixels. of all these pixels. of all these pixels.

    So this is the architecture for the So this is the architecture for the So this
    is the architecture for the

    decoder network. decoder network. decoder network.

    [snorts] And finally uh you have a [snorts] And finally uh you have a [snorts]
    And finally uh you have a

    sigmoid so that you convert that into a sigmoid so that you convert that into
    a sigmoid so that you convert that into a

    probability value. So we only have the decoder architecture So we only have the
    decoder architecture

    which is the second machine. Now we want which is the second machine. Now we want
    which is the second machine. Now we want

    the first machine also. What does the the first machine also. What does the the
    first machine also. What does the

    first machine do? The first machine first machine do? The first machine'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 78
  start_sec: 4747.92
  end_sec: 4813.03
  text: 'first machine do? The first machine

    actually does the reverse. It takes the actually does the reverse. It takes the
    actually does the reverse. It takes the

    image as the input, the real image, and image as the input, the real image, and
    image as the input, the real image, and

    it gives the Latin space as the output, it gives the Latin space as the output,
    it gives the Latin space as the output,

    the sample in the latent space. the sample in the latent space. the sample in
    the latent space.

    Now, so it has the input has 784 values, Now, so it has the input has 784 values,
    Now, so it has the input has 784 values,

    right? 28x 28. right? 28x 28. right? 28x 28.

    But what is the output here? But what is the output here? But what is the output
    here?

    Is it deterministic or probabilistic? Is it deterministic or probabilistic? Is
    it deterministic or probabilistic?

    As we had discussed the variational part As we had discussed the variational part
    As we had discussed the variational part

    of the VA means that the output is of the VA means that the output is of the VA
    means that the output is

    probabilistic. So for every probabilistic. So for every probabilistic. So for
    every

    so you can argue that okay maybe there so you can argue that okay maybe there
    so you can argue that okay maybe there

    are only two values here right only two are only two values here right only two
    are only two values here right only two

    right but then right but then right but then

    there are two values for two means and there are two values for two means and
    there are two values for two means and

    there are two values for two standard there are two values for two standard there
    are two values for two standard

    deviations. So overall there are four deviations. So overall there are four deviations.
    So overall there are four

    values which this encoder network gives values which this encoder network gives
    values which this encoder network gives

    as an output. as an output. as an output.

    So the the image three might map to this So the the image three might map to this
    So the the image three might map to this

    region which has the mu of.5 comma.5 and'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 79
  start_sec: 4813.03
  end_sec: 4861.189
  text: 'region which has the mu of.5 comma.5 and region which has the mu of.5 comma.5
    and

    the sigma of 2a 2. Right? So you need the sigma of 2a 2. Right? So you need the
    sigma of 2a 2. Right? So you need

    two mu values and two sigma values to two mu values and two sigma values to two
    mu values and two sigma values to

    create the mapping in the latent space. create the mapping in the latent space.
    create the mapping in the latent space.

    This is why the word variational in the This is why the word variational in the
    This is why the word variational in the

    variational autoenccoder comes. So the variational autoenccoder comes. So the
    variational autoenccoder comes. So the

    encoder network should do the following. encoder network should do the following.
    encoder network should do the following.

    It should take the input and generate It should take the input and generate It
    should take the input and generate

    two mean values and two standard two mean values and two standard two mean values
    and two standard

    deviation values. deviation values. deviation values.

    And we use the following architecture And we use the following architecture And
    we use the following architecture

    for the encoder. We have 784 nodes as for the encoder. We have 784 nodes as for
    the encoder. We have 784 nodes as

    the input. Again, we have 400 nodes as the input. Again, we have 400 nodes as
    the input. Again, we have 400 nodes as

    the hidden layer. But as the output, we the hidden layer. But as the output, we
    the hidden layer. But as the output, we

    have two nodes for the mean and two have two nodes for the mean and two have two
    nodes for the mean and two

    nodes for the logarithm of the variance. nodes for the logarithm of the variance.
    nodes for the logarithm of the variance.

    Now, why we we need this logarithm? it Now, why we we need this logarithm? it
    Now, why we we need this logarithm? it

    will become clear uh in the Google will become clear uh in the Google will become
    clear uh in the Google

    collab notebook which I will share in collab notebook which I will share in collab
    notebook which I will share in

    the GitHub repo in the description'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 80
  start_sec: 4861.189
  end_sec: 4916.95
  text: 'the GitHub repo in the description the GitHub repo in the description

    section. section. section.

    [snorts] [snorts]

    Okay. So overall the encoder decoder Okay. So overall the encoder decoder Okay.
    So overall the encoder decoder

    architecture looks as follows. The architecture looks as follows. The architecture
    looks as follows. The

    encoder takes the image and uh goes encoder takes the image and uh goes encoder
    takes the image and uh goes

    through the hidden layer and generates through the hidden layer and generates
    through the hidden layer and generates

    the the

    mean and the variance. So this is the mean and the variance. So this is the mean
    and the variance. So this is the

    latent space variables. latent space variables. latent space variables.

    How do you generate the latent variable How do you generate the latent variable
    How do you generate the latent variable

    from this? You take the mean and you do from this? You take the mean and you do
    from this? You take the mean and you do

    mu + sigma into epsilon where epsilon is mu + sigma into epsilon where epsilon
    is mu + sigma into epsilon where epsilon is

    any value between 0 and 1. So that''s how any value between 0 and 1. So that''s
    how any value between 0 and 1. So that''s how

    you sample from this latent space you sample from this latent space you sample
    from this latent space

    and then you pass this latent variable and then you pass this latent variable
    and then you pass this latent variable

    as an input to the decoder network which as an input to the decoder network which
    as an input to the decoder network which

    generates your output. generates your output. generates your output.

    So this is something which your mu and So this is something which your mu and
    So this is something which your mu and

    variance will only give you a variance will only give you a variance will only
    give you a

    distribution but you need to sample from distribution but you need to sample from
    distribution but you need to sample from

    that distribution. Right? This is done that distribution. Right? This is done
    that distribution. Right? This is done

    by this simple formula over here. by this simple formula over here. by this simple
    formula over here.

    So this is our entire encoder decoder'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 81
  start_sec: 4916.95
  end_sec: 4971.84
  text: 'So this is our entire encoder decoder So this is our entire encoder decoder

    architecture whatever we discussed as architecture whatever we discussed as architecture
    whatever we discussed as

    this machine. this machine. this machine.

    uh now we are able to put it in an uh now we are able to put it in an uh now we
    are able to put it in an

    actual mathematical neural network which actual mathematical neural network which
    actual mathematical neural network which

    is very interesting because we are going is very interesting because we are going
    is very interesting because we are going

    from a conceptual explanation to an from a conceptual explanation to an from a
    conceptual explanation to an

    actual practical implementation. So it actual practical implementation. So it
    actual practical implementation. So it

    should make everything clear in your should make everything clear in your should
    make everything clear in your

    mind. mind. mind.

    Now the next thing to discuss is how do Now the next thing to discuss is how do
    Now the next thing to discuss is how do

    we we we

    uh define the elbow loss and how do we uh define the elbow loss and how do we
    uh define the elbow loss and how do we

    train this encoder decoder architecture. train this encoder decoder architecture.
    train this encoder decoder architecture.

    Okay. So let''s understand how the elbow Okay. So let''s understand how the elbow
    Okay. So let''s understand how the elbow

    loss is defined. [clears throat] loss is defined. [clears throat] loss is defined.
    [clears throat]

    Remember the elbow loss is made up of Remember the elbow loss is made up of Remember
    the elbow loss is made up of

    two terms. The reconstruction loss and two terms. The reconstruction loss and
    two terms. The reconstruction loss and

    the regularization term. the regularization term. the regularization term.

    Now the goal of the reconstruction loss Now the goal of the reconstruction loss
    Now the goal of the reconstruction loss

    is to make the output image look exactly is to make the output image look exactly
    is to make the output image look exactly

    the same as the input image. the same as the input image. the same as the input
    image.

    This compares every pixel of the input This compares every pixel of the input'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 82
  start_sec: 4971.84
  end_sec: 5026.4
  text: 'This compares every pixel of the input

    with the output. If the original pixel with the output. If the original pixel
    with the output. If the original pixel

    is black and the VA predicts white, the is black and the VA predicts white, the
    is black and the VA predicts white, the

    penalty is huge. If the VA predicts penalty is huge. If the VA predicts penalty
    is huge. If the VA predicts

    correctly, the penalty is low. Hence the correctly, the penalty is low. Hence
    the correctly, the penalty is low. Hence the

    reconstruction loss is written as a reconstruction loss is written as a reconstruction
    loss is written as a

    simple binary cross entropy loss between simple binary cross entropy loss between
    simple binary cross entropy loss between

    the true image and the predicted image. the true image and the predicted image.
    the true image and the predicted image.

    So the reconstruction loss is simply So the reconstruction loss is simply So the
    reconstruction loss is simply

    comparing the two images and seeing okay comparing the two images and seeing okay
    comparing the two images and seeing okay

    what is what are the differences in the what is what are the differences in the
    what is what are the differences in the

    probabilities between the two images and probabilities between the two images
    and probabilities between the two images and

    we don''t just subtract these we don''t just subtract these we don''t just subtract
    these

    probabilities we do a binary cross probabilities we do a binary cross probabilities
    we do a binary cross

    entropy loss. entropy loss. entropy loss.

    The second term is the kale divergence The second term is the kale divergence
    The second term is the kale divergence

    loss. [snorts] Now this is something loss. [snorts] Now this is something loss.
    [snorts] Now this is something

    where the objective of the kale where the objective of the kale where the objective
    of the kale

    divergence loss is to make sure that the latin space to make sure that the latin
    space

    distribution has a mean of has a mean of distribution has a mean of has a mean
    of distribution has a mean of has a mean of

    zero and a standard deviation of one. To zero and a standard deviation of one.
    To'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 83
  start_sec: 5026.4
  end_sec: 5080.159
  text: 'zero and a standard deviation of one. To

    ensure that the mean is zero, we add a ensure that the mean is zero, we add a
    ensure that the mean is zero, we add a

    penalty if the mean deviates from zero. penalty if the mean deviates from zero.
    penalty if the mean deviates from zero.

    So this mean So this mean So this mean

    that we are talking about uh this mean that we are talking about uh this mean
    that we are talking about uh this mean

    mu. mu. mu.

    So the first loss term is mu squared. So So the first loss term is mu squared.
    So So the first loss term is mu squared. So

    if the mean deviates from zero, we add a if the mean deviates from zero, we add
    a if the mean deviates from zero, we add a

    penalty. Similarly, if the standard penalty. Similarly, if the standard penalty.
    Similarly, if the standard

    deviation is huge, the model is deviation is huge, the model is deviation is huge,
    the model is

    penalized for being too messy. And if penalized for being too messy. And if penalized
    for being too messy. And if

    the standard deviation is too tiny, then the standard deviation is too tiny, then
    the standard deviation is too tiny, then

    also the model is specified for being also the model is specified for being also
    the model is specified for being

    too specific. too specific. too specific.

    So the penalty looks as follows. So the penalty looks as follows. So the penalty
    looks as follows.

    Sigma square because we want to penalize Sigma square because we want to penalize
    Sigma square because we want to penalize

    if the variance is huge. So this becomes if the variance is huge. So this becomes
    if the variance is huge. So this becomes

    huge if variance is large. So the model huge if variance is large. So the model
    huge if variance is large. So the model

    is penalized. And if the variance is is penalized. And if the variance is is penalized.
    And if the variance is

    very small then this becomes huge very small then this becomes huge very small
    then this becomes huge

    because log of a small value is a big uh because log of a small value is a big
    uh'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 84
  start_sec: 5080.159
  end_sec: 5134.48
  text: 'because log of a small value is a big uh

    number and there is a negative sign number and there is a negative sign number
    and there is a negative sign

    associated with it. So this will always associated with it. So this will always
    associated with it. So this will always

    ensure that the variance stays ensure that the variance stays ensure that the
    variance stays

    close to one. So this is what we want. close to one. So this is what we want.
    close to one. So this is what we want.

    So this is very clear mu square where So this is very clear mu square where So
    this is very clear mu square where

    the center has the minimum penalty cost the center has the minimum penalty cost
    the center has the minimum penalty cost

    but this function variance minus but this function variance minus but this function
    variance minus

    log of variance minus one. log of variance minus one. log of variance minus one.

    This means that you will always you you This means that you will always you you
    This means that you will always you you

    want the the variance to be as close to want the the variance to be as close to
    want the the variance to be as close to

    one as possible which is what this is uh one as possible which is what this is
    uh one as possible which is what this is uh

    achieving. you''re you''re penalizing for achieving. you''re you''re penalizing
    for achieving. you''re you''re penalizing for

    the variance becoming too small and you the variance becoming too small and you
    the variance becoming too small and you

    you''re penalizing for the variance you''re penalizing for the variance you''re
    penalizing for the variance

    becoming too big. becoming too big. becoming too big.

    Now you will see all of this very nicely Now you will see all of this very nicely
    Now you will see all of this very nicely

    written in this Google Collab notebook written in this Google Collab notebook
    written in this Google Collab notebook

    which I will share with all of you in which I will share with all of you in which
    I will share with all of you in

    the uh description. But first I just the uh description. But first I just'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 85
  start_sec: 5134.48
  end_sec: 5186.31
  text: 'the uh description. But first I just

    want to want to want to

    describe everything that we have describe everything that we have describe everything
    that we have

    conceptually described in a mathematical conceptually described in a mathematical
    conceptually described in a mathematical

    framework so that every single concept framework so that every single concept
    framework so that every single concept

    is clear. is clear. is clear.

    Now next what we do is we train the Now next what we do is we train the Now next
    what we do is we train the

    variational autoenccoder. variational autoenccoder.

    So uh this is a GIF I have created. Let So uh this is a GIF I have created. Let
    So uh this is a GIF I have created. Let

    me play this. You can see that as we me play this. You can see that as we me play
    this. You can see that as we

    train it the objective is for the Z1 train it the objective is for the Z1 train
    it the objective is for the Z1

    distribution and zed2 distribution to distribution and zed2 distribution to distribution
    and zed2 distribution to

    become as close as possible to a gshian become as close as possible to a gshian
    become as close as possible to a gshian

    which is exactly what is happening. This which is exactly what is happening. This
    which is exactly what is happening. This

    is because of this term where the mu is is because of this term where the mu is
    is because of this term where the mu is

    forced to be close to zero and variance forced to be close to zero and variance
    forced to be close to zero and variance

    is forced to be close to one. is forced to be close to one. is forced to be close
    to one.

    So the latin space finally looks So the latin space finally looks So the latin
    space finally looks

    something like this something like this something like this

    where you can see that it''s not exactly where you can see that it''s not exactly
    where you can see that it''s not exactly

    has a variance of one but if if we train has a variance of one but if if we train
    has a variance of one but if if we train

    for longer duration maybe we''ll get an'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 86
  start_sec: 5186.31
  end_sec: 5241.75
  text: 'for longer duration maybe we''ll get an for longer duration maybe we''ll
    get an

    even better distribution which is even better distribution which is even better
    distribution which is

    centered at zero and distributed around centered at zero and distributed around
    centered at zero and distributed around

    one. But there are clusters uh there are one. But there are clusters uh there
    are one. But there are clusters uh there are

    clusters which are formed for every clusters which are formed for every clusters
    which are formed for every

    digit. For example, you can see this digit. For example, you can see this digit.
    For example, you can see this

    orange cluster represents digit one. The orange cluster represents digit one.
    The orange cluster represents digit one. The

    blue cluster represents digit blue cluster represents digit blue cluster represents
    digit

    zero. Green represents two, etc. Which zero. Green represents two, etc. Which
    zero. Green represents two, etc. Which

    is very beautiful in a way, right? is very beautiful in a way, right? is very
    beautiful in a way, right?

    Because in using only two variables, you Because in using only two variables,
    you Because in using only two variables, you

    are able to compress the handwritten are able to compress the handwritten are
    able to compress the handwritten

    digits and digits and digits and

    there are intersections in some cases. there are intersections in some cases.
    there are intersections in some cases.

    But that is expected because you have But that is expected because you have But
    that is expected because you have

    only two variables. So there will be only two variables. So there will be only
    two variables. So there will be

    intersections intersections intersections

    but still this is the latent space. but still this is the latent space. but still
    this is the latent space.

    These are the hidden factors of These are the hidden factors of These are the
    hidden factors of

    variation and we have forced the latin variation and we have forced the latin
    variation and we have forced the latin

    space distribution to be as close as space distribution to be as close as space
    distribution to be as close as

    possible to the gshian as you see as possible to the gshian as you see as possible
    to the gshian as you see as

    this training proceeds and this is the'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 87
  start_sec: 5241.75
  end_sec: 5295.04
  text: 'this training proceeds and this is the this training proceeds and this is
    the

    quality of the reconstructions because quality of the reconstructions because
    quality of the reconstructions because

    we have the reconstruction loss. We see we have the reconstruction loss. We see
    we have the reconstruction loss. We see

    that the reconstruction is as close as that the reconstruction is as close as
    that the reconstruction is as close as

    possible to the true uh to the true possible to the true uh to the true possible
    to the true uh to the true

    variable. variable. variable.

    Another point I I I forgot to mention in Another point I I I forgot to mention
    in Another point I I I forgot to mention in

    the Latin space is that you can see that the Latin space is that you can see that
    the Latin space is that you can see that

    the Latin space is now somewhat the Latin space is now somewhat the Latin space
    is now somewhat

    continuous. It is not disjoint. continuous. It is not disjoint. continuous. It
    is not disjoint.

    In a pure autoenccoder, there won''t be In a pure autoenccoder, there won''t be
    In a pure autoenccoder, there won''t be

    single points which will be which will single points which will be which will
    single points which will be which will

    correspond to single digits. But you correspond to single digits. But you correspond
    to single digits. But you

    won''t get a like for example this entire won''t get a like for example this entire
    won''t get a like for example this entire

    region corresponds to number one region corresponds to number one region corresponds
    to number one

    which is exactly how we have trained the which is exactly how we have trained
    the which is exactly how we have trained the

    encoder. encoder.

    And this entire region is where you will And this entire region is where you will
    And this entire region is where you will

    see all the data to be scattered. see all the data to be scattered. see all the
    data to be scattered.

    Okay. And then if you sample from the Okay. And then if you sample from the Okay.
    And then if you sample from the

    latin space uh you see that the it''s latin space uh you see that the it''s'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 88
  start_sec: 5295.04
  end_sec: 5345.76
  text: 'latin space uh you see that the it''s

    it''s kind of blur in some cases which it''s kind of blur in some cases which
    it''s kind of blur in some cases which

    we''ll come to in in in some time but you we''ll come to in in in some time but
    you we''ll come to in in in some time but you

    get realistic almost realistic get realistic almost realistic get realistic almost
    realistic

    handwritten uh digits. You have a five handwritten uh digits. You have a five
    handwritten uh digits. You have a five

    here. You have a six. you have an 8 9 7 here. You have a six. you have an 8 9
    7 here. You have a six. you have an 8 9 7

    1 0. 1 0. 1 0.

    So it''s it''s a very beautiful practical So it''s it''s a very beautiful practical
    So it''s it''s a very beautiful practical

    example which is explained in this example which is explained in this example
    which is explained in this

    Google collab notebook. I will share the Google collab notebook. I will share
    the Google collab notebook. I will share the

    link uh in in the description along with link uh in in the description along with
    link uh in in the description along with

    the GitHub repo. You''ll be able to the GitHub repo. You''ll be able to the GitHub
    repo. You''ll be able to

    understand all the details. Uh I have understand all the details. Uh I have understand
    all the details. Uh I have

    explained the things. This is the elbow explained the things. This is the elbow
    explained the things. This is the elbow

    loss which I have explained. This is the loss which I have explained. This is
    the loss which I have explained. This is the

    encoder decoder architecture and then encoder decoder architecture and then encoder
    decoder architecture and then

    the training process and the results. the training process and the results. the
    training process and the results.

    >> [snorts] >> [snorts]

    >> uh one of the drawbacks of standard VAE >> uh one of the drawbacks of standard
    VAE >> uh one of the drawbacks of standard VAE

    is that it it produces blurry outputs is that it it produces blurry outputs'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 89
  start_sec: 5345.76
  end_sec: 5397.76
  text: 'is that it it produces blurry outputs

    and there is a very nice reason for it. and there is a very nice reason for it.
    and there is a very nice reason for it.

    I will share the link in the description I will share the link in the description
    I will share the link in the description

    why it produces blurry outputs but uh why it produces blurry outputs but uh why
    it produces blurry outputs but uh

    that''s that''s one of the main drawbacks that''s that''s one of the main drawbacks
    that''s that''s one of the main drawbacks

    of this framework. of this framework. of this framework.

    And another challenge is that you have And another challenge is that you have
    And another challenge is that you have

    to train two networks. You have to train to train two networks. You have to train
    to train two networks. You have to train

    an encoder network and you have to train an encoder network and you have to train
    an encoder network and you have to train

    a decoder network. So the joint training a decoder network. So the joint training
    a decoder network. So the joint training

    sometimes becomes very challenging and sometimes becomes very challenging and
    sometimes becomes very challenging and

    the learning becomes unstable the learning becomes unstable the learning becomes
    unstable

    and this is exactly what diffusion and this is exactly what diffusion and this
    is exactly what diffusion

    models learn to sidestep this central models learn to sidestep this central models
    learn to sidestep this central

    weakness which is what we will learn in weakness which is what we will learn in
    weakness which is what we will learn in

    the next lecture. the next lecture. the next lecture.

    So uh this is all about variational So uh this is all about variational So uh
    this is all about variational

    autoenccoders. This technique has become autoenccoders. This technique has become
    autoenccoders. This technique has become

    very popular in not just diffusion but very popular in not just diffusion but
    very popular in not just diffusion but

    also in robotics in a lot of different also in robotics in a lot of different
    also in robotics in a lot of different

    applications I have seen and uh there applications I have seen and uh there'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
- idx: 90
  start_sec: 5397.76
  end_sec: 5439.36
  text: 'applications I have seen and uh there

    are encoders and distribute and and are encoders and distribute and and are encoders
    and distribute and and

    decoders right so you also have decoders right so you also have decoders right
    so you also have

    different architectures for them for different architectures for them for different
    architectures for them for

    example here we looked at neural example here we looked at neural example here
    we looked at neural

    networks plain neural networks simple networks plain neural networks simple networks
    plain neural networks simple

    neural networks but you can also have a neural networks but you can also have
    a neural networks but you can also have a

    transformer encoder and a transformer transformer encoder and a transformer transformer
    encoder and a transformer

    decoder inside a VAE so once you decoder inside a VAE so once you decoder inside
    a VAE so once you

    understand this uh vanilla setup you can understand this uh vanilla setup you
    can understand this uh vanilla setup you can

    understand every other setup which you understand every other setup which you
    understand every other setup which you

    read in different research papers but read in different research papers but read
    in different research papers but

    this is going to form a very nice this is going to form a very nice this is going
    to form a very nice

    foundation for us as we discuss about foundation for us as we discuss about foundation
    for us as we discuss about

    diffusion models going forward. Thank diffusion models going forward. Thank diffusion
    models going forward. Thank

    you very much everyone and I hope you you very much everyone and I hope you you
    very much everyone and I hope you

    are liking these lectures. Uh and I''ll are liking these lectures. Uh and I''ll
    are liking these lectures. Uh and I''ll

    I''ll meet you in the next lecture. Thank I''ll meet you in the next lecture.
    Thank I''ll meet you in the next lecture. Thank

    you.'
  concept_slugs:
  - reparameterization-trick
  - vae-encoder
  - variational-lower-bound
---
# Lecture 2 - Variational Autoencoders Explained From Scratch | Principles of Diffusion Models

See the structured chunks above.
