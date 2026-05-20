---
course_slug: diffusion-principles-vizuara
idx: 8
title: Lecture 3 - Introduction to Diffusion Models (DDPM) | Principles of Diffusion
  Models
video_url: https://www.youtube.com/watch?v=Dx-1agEjlJs
duration_sec: null
chunks:
- idx: 0
  start_sec: 5.749
  end_sec: 70.39
  text: 'Hello everyone and welcome to the third Hello everyone and welcome to the
    third

    lecture of this course principles of lecture of this course principles of lecture
    of this course principles of

    diffusion models. diffusion models. diffusion models.

    It''s taking me some time to release It''s taking me some time to release It''s
    taking me some time to release

    these lectures because the preparation these lectures because the preparation
    these lectures because the preparation

    time is increasing for each lectures. I time is increasing for each lectures.
    I time is increasing for each lectures. I

    hope all of you stay patient and uh stay hope all of you stay patient and uh stay
    hope all of you stay patient and uh stay

    with me throughout this course. with me throughout this course. with me throughout
    this course.

    In this particular lecture, we are going In this particular lecture, we are going
    In this particular lecture, we are going

    to move forward from variational to move forward from variational to move forward
    from variational

    autoenccoders. autoenccoders. autoenccoders.

    Before we move ahead, I want to do a Before we move ahead, I want to do a Before
    we move ahead, I want to do a

    quick recap of variation autoenccoders quick recap of variation autoenccoders
    quick recap of variation autoenccoders

    and what is the exact architecture of and what is the exact architecture of and
    what is the exact architecture of

    VAEEs. VAEEs. VAEEs.

    So, VAEs have an architecture which look So, VAEs have an architecture which look
    So, VAEs have an architecture which look

    like this. you have a data and then you like this. you have a data and then you
    like this. you have a data and then you

    have an encoder which transforms this have an encoder which transforms this have
    an encoder which transforms this

    data from the real space to the latent data from the real space to the latent
    data from the real space to the latent

    space. space. space.

    Now why is this transformation done? The Now why is this transformation done?
    The Now why is this transformation done? The

    reason this transformation is done is reason this transformation is done is reason
    this transformation is done is

    because you need something to capture because you need something to capture because
    you need something to capture

    the the the

    hidden factors or the factors which'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 1
  start_sec: 70.39
  end_sec: 132.239
  text: 'hidden factors or the factors which hidden factors or the factors which

    affect the variation in the data. For affect the variation in the data. For affect
    the variation in the data. For

    example, if we look at the handwriting example, if we look at the handwriting
    example, if we look at the handwriting

    styles of all the students in a class, styles of all the students in a class,
    styles of all the students in a class,

    there might be certain specific factors there might be certain specific factors
    there might be certain specific factors

    which influence the handwriting style which influence the handwriting style which
    influence the handwriting style

    like how neat the handwriting is or how like how neat the handwriting is or how
    like how neat the handwriting is or how

    slanted the handwriting is. These are slanted the handwriting is. These are slanted
    the handwriting is. These are

    the hidden factors which the hidden factors which the hidden factors which

    influence the variation in the data. Now influence the variation in the data.
    Now influence the variation in the data. Now

    what the encoder does is that the what the encoder does is that the what the encoder
    does is that the

    encoder maps the data from real space to encoder maps the data from real space
    to encoder maps the data from real space to

    the latin space which is usually of the latin space which is usually of the latin
    space which is usually of

    less number of dimensions compared to less number of dimensions compared to less
    number of dimensions compared to

    the real data. For example, if we pick the real data. For example, if we pick
    the real data. For example, if we pick

    handwritten digits and we arrange them handwritten digits and we arrange them
    handwritten digits and we arrange them

    in a grid of 28x 28 that is 784 pixels. in a grid of 28x 28 that is 784 pixels.
    in a grid of 28x 28 that is 784 pixels.

    So you have 784 dimensions to represent So you have 784 dimensions to represent
    So you have 784 dimensions to represent

    each handwritten digit. But you can each handwritten digit. But you can each handwritten
    digit. But you can

    transform them into a Latin space with transform them into a Latin space with'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 2
  start_sec: 132.239
  end_sec: 195.27
  text: 'transform them into a Latin space with

    only two dimensions X and Y data. only two dimensions X and Y data. only two dimensions
    X and Y data.

    The Latin space the intuition behind The Latin space the intuition behind The
    Latin space the intuition behind

    Latin space is that Latin space is that Latin space is that

    it captures the hidden factors of of it captures the hidden factors of of it captures
    the hidden factors of of

    variation. variation. variation.

    Now since you''re compressing the data Now since you''re compressing the data
    Now since you''re compressing the data

    this much, you are bound to lose this much, you are bound to lose this much, you
    are bound to lose

    something. you''re bound to lose some something. you''re bound to lose some something.
    you''re bound to lose some

    information information information

    but the idea is that we capture the but the idea is that we capture the but the
    idea is that we capture the

    necessary information so that it is good necessary information so that it is good
    necessary information so that it is good

    enough for us to be able to reproduce enough for us to be able to reproduce enough
    for us to be able to reproduce

    the data. Okay. [clears throat] So now we have Okay. [clears throat] So now we
    have

    looked at the first step which is the looked at the first step which is the looked
    at the first step which is the

    encoder which encodes the data. It is encoder which encodes the data. It is encoder
    which encodes the data. It is

    similar to uh let''s take the same similar to uh let''s take the same similar
    to uh let''s take the same

    example of handwriting styles. you have example of handwriting styles. you have
    example of handwriting styles. you have

    a map in the Latin space which says that a map in the Latin space which says that
    a map in the Latin space which says that

    this point corresponds to this student''s this point corresponds to this student''s
    this point corresponds to this student''s

    handwriting. This point corresponds to handwriting. This point corresponds to
    handwriting. This point corresponds to

    this students handwriting etc. So it''s this students handwriting etc. So it''s
    this students handwriting etc. So it''s

    it''s also called as a style variable'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 3
  start_sec: 195.27
  end_sec: 254.159
  text: 'it''s also called as a style variable it''s also called as a style variable

    because it captures the style which is because it captures the style which is
    because it captures the style which is

    inherent in your real data distribution. inherent in your real data distribution.
    inherent in your real data distribution.

    [snorts] Okay. So the encoder captures [snorts] Okay. So the encoder captures
    [snorts] Okay. So the encoder captures

    the hidden factors of variation. the hidden factors of variation. the hidden factors
    of variation.

    U what next? U what next? U what next?

    Well, you don''t want to just capture the Well, you don''t want to just capture
    the Well, you don''t want to just capture the

    hidden factors of variation, but you hidden factors of variation, but you hidden
    factors of variation, but you

    want to reproduce the want to reproduce the want to reproduce the

    original image as well, right? And that original image as well, right? And that
    original image as well, right? And that

    is exactly what the decoder does. So is exactly what the decoder does. So is exactly
    what the decoder does. So

    imagine you have a typing machine where imagine you have a typing machine where
    imagine you have a typing machine where

    you type in these latent variables, you type in these latent variables, you type
    in these latent variables,

    let''s say zed 1, zed 2, and then the let''s say zed 1, zed 2, and then the let''s
    say zed 1, zed 2, and then the

    machine gives you a print out of the machine gives you a print out of the machine
    gives you a print out of the

    original image. original image. original image.

    So you mention the style variables and So you mention the style variables and
    So you mention the style variables and

    every single style variable maps every single style variable maps every single
    style variable maps

    uniquely uniquely uniquely

    to an image of an handwriting let''s say. to an image of an handwriting let''s
    say. to an image of an handwriting let''s say.

    So you type in those style variables and So you type in those style variables
    and So you type in those style variables and

    you get the image out of it. That is you get the image out of it. That is'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 4
  start_sec: 254.159
  end_sec: 325.199
  text: 'you get the image out of it. That is

    this machine is called as the decoder. this machine is called as the decoder.
    this machine is called as the decoder.

    So the decoder takes in the latent So the decoder takes in the latent So the decoder
    takes in the latent

    variable or the latent representation as variable or the latent representation
    as variable or the latent representation as

    an input and it predicts the image as an an input and it predicts the image as
    an an input and it predicts the image as an

    output or it predicts the output or it predicts the output or it predicts the

    data as an output which is supposed to data as an output which is supposed to
    data as an output which is supposed to

    match as much as possible to the real match as much as possible to the real match
    as much as possible to the real

    data which is fed to the encoder. Now the question is uh you have this Now the
    question is uh you have this

    pipeline right? You have pipeline which pipeline right? You have pipeline which
    pipeline right? You have pipeline which

    looks like this. looks like this. looks like this.

    You have an encoder which maps the real You have an encoder which maps the real
    You have an encoder which maps the real

    data to some areas of the Latin space data to some areas of the Latin space data
    to some areas of the Latin space

    and then you have a decoder which maps and then you have a decoder which maps
    and then you have a decoder which maps

    it back to the real space. it back to the real space. it back to the real space.

    So this is something which is also So this is something which is also So this
    is something which is also

    called as an autoenccoder. called as an autoenccoder. called as an autoenccoder.

    But where does the name variational come But where does the name variational come
    But where does the name variational come

    into the picture? into the picture? into the picture?

    The name variational comes in because The name variational comes in because The
    name variational comes in because

    when we map the word hello into the when we map the word hello into the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 5
  start_sec: 325.199
  end_sec: 388.639
  text: 'when we map the word hello into the

    areas of the Latin space, we don''t just areas of the Latin space, we don''t just
    areas of the Latin space, we don''t just

    map it to one single value, but we map map it to one single value, but we map
    map it to one single value, but we map

    it to a distribution. So basically we it to a distribution. So basically we it
    to a distribution. So basically we

    say that say that say that

    the word hello has the highest the word hello has the highest the word hello has
    the highest

    probability of being here but it can probability of being here but it can probability
    of being here but it can

    also be in this entire circle can be also be in this entire circle can be also
    be in this entire circle can be

    anywhere within this circle. So you are mapping the data to specific So you are
    mapping the data to specific

    areas of the latin space. You don''t map areas of the latin space. You don''t
    map areas of the latin space. You don''t map

    it to specific points. it to specific points. it to specific points.

    And the reason we do this is because And the reason we do this is because And
    the reason we do this is because

    this allows you to have a Latin space this allows you to have a Latin space this
    allows you to have a Latin space

    which which which

    semantically means something. Otherwise, semantically means something. Otherwise,
    semantically means something. Otherwise,

    you will have individual points meaning you will have individual points meaning
    you will have individual points meaning

    something specific. But the region something specific. But the region something
    specific. But the region

    between those points won''t mean between those points won''t mean between those
    points won''t mean

    anything. It it it won''t capture any anything. It it it won''t capture any anything.
    It it it won''t capture any

    semantics at all. semantics at all. semantics at all.

    We looked at an example of uh We looked at an example of uh We looked at an example
    of uh

    reproducing handwritten digits and there reproducing handwritten digits and there
    reproducing handwritten digits and there

    we saw the Latin space after the we saw the Latin space after the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 6
  start_sec: 388.639
  end_sec: 449.12
  text: 'we saw the Latin space after the

    training is completed. It looks training is completed. It looks training is completed.
    It looks

    something like this. something like this. something like this.

    Now Now Now

    this these areas in the Latin space this these areas in the Latin space this these
    areas in the Latin space

    corresponds to digits. For example, this corresponds to digits. For example, this
    corresponds to digits. For example, this

    area corresponds to digit one. This area area corresponds to digit one. This area
    area corresponds to digit one. This area

    corresponds to digit zero etc. So corresponds to digit zero etc. So corresponds
    to digit zero etc. So

    instead of mapping the data to single instead of mapping the data to single instead
    of mapping the data to single

    point, we now have areas in the latent point, we now have areas in the latent
    point, we now have areas in the latent

    space or probability distribution. space or probability distribution. space or
    probability distribution.

    So because we map it to a distribution So because we map it to a distribution
    So because we map it to a distribution

    and not a single point, we have a and not a single point, we have a and not a
    single point, we have a

    variational autoenccoder. variational autoenccoder. variational autoenccoder.

    And people found out that the moment you And people found out that the moment
    you And people found out that the moment you

    do that the accuracy of generating do that the accuracy of generating do that
    the accuracy of generating

    images as if they are sampled from the images as if they are sampled from the
    images as if they are sampled from the

    real data increases by a big order of real data increases by a big order of real
    data increases by a big order of

    magnitude. So it makes a lot of magnitude. So it makes a lot of magnitude. So
    it makes a lot of

    difference. Okay. So u you have an encoder which Okay. So u you have an encoder
    which

    maps it to these areas of the Latin maps it to these areas of the Latin maps it
    to these areas of the Latin

    space. You have a decoder which maps it space. You have a decoder which maps it'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 7
  start_sec: 449.12
  end_sec: 512.159
  text: 'space. You have a decoder which maps it

    back. How do you train the variation back. How do you train the variation back.
    How do you train the variation

    autoenccoder? What''s the process that autoenccoder? What''s the process that
    autoenccoder? What''s the process that

    you follow for training? you follow for training? you follow for training?

    Now the first thing that might come to Now the first thing that might come to
    Now the first thing that might come to

    your mind is this is straightforward. I your mind is this is straightforward.
    I your mind is this is straightforward. I

    just need to make sure that the output just need to make sure that the output
    just need to make sure that the output

    is same as the input. So I need to is same as the input. So I need to is same
    as the input. So I need to

    reduce the uh difference between the reduce the uh difference between the reduce
    the uh difference between the

    output image and the input image. output image and the input image. output image
    and the input image.

    And this is sort of correct. uh this is And this is sort of correct. uh this is
    And this is sort of correct. uh this is

    one part of the loss which is called as one part of the loss which is called as
    one part of the loss which is called as

    the reconstruction loss. the reconstruction loss. the reconstruction loss.

    But in variational autoenccoder we have But in variational autoenccoder we have
    But in variational autoenccoder we have

    another loss which is called as the another loss which is called as the another
    loss which is called as the

    regularization loss. regularization loss. regularization loss.

    What the regularization loss does is it What the regularization loss does is it
    What the regularization loss does is it

    makes sure that the latin space the latin space

    the final distribution in the latin the final distribution in the latin the final
    distribution in the latin

    space space space

    has a mean of zero and a variance of has a mean of zero and a variance of has
    a mean of zero and a variance of

    one. So it it it''s a gshian one. So it it it''s a gshian one. So it it it''s
    a gshian

    distribution. distribution.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 8
  start_sec: 512.159
  end_sec: 571.75
  text: 'distribution.

    So it tries to move the distribution in So it tries to move the distribution in
    So it tries to move the distribution in

    the latin space to a gshian the latin space to a gshian the latin space to a gshian

    distribution. Now here you see it distribution. Now here you see it distribution.
    Now here you see it

    doesn''t really appear like a gshian doesn''t really appear like a gshian doesn''t
    really appear like a gshian

    right because it''s kind of right because it''s kind of right because it''s kind
    of

    spread out and it''s spread out even spread out and it''s spread out even spread
    out and it''s spread out even

    beyond minus1 and + one which leads me beyond minus1 and + one which leads me
    beyond minus1 and + one which leads me

    to believe that the standard deviation to believe that the standard deviation
    to believe that the standard deviation

    here is maybe greater than one maybe two here is maybe greater than one maybe
    two here is maybe greater than one maybe two

    or three times. So it''s not exactly or three times. So it''s not exactly or three
    times. So it''s not exactly

    compressing it to a region of mean zero compressing it to a region of mean zero
    compressing it to a region of mean zero

    and a variance of one. and a variance of one. and a variance of one.

    But it tries to do that. It it tries to But it tries to do that. It it tries to
    But it tries to do that. It it tries to

    compress the latin space into this compress the latin space into this compress
    the latin space into this

    gshian distribution. And uh my intuition gshian distribution. And uh my intuition
    gshian distribution. And uh my intuition

    why that is done is I I feel that every why that is done is I I feel that every
    why that is done is I I feel that every

    single hidden factors of variation single hidden factors of variation single hidden
    factors of variation

    underlying any data it satisfies a underlying any data it satisfies a underlying
    any data it satisfies a

    gshian. gshian. gshian.

    Take an example of handwriting samples Take an example of handwriting samples
    Take an example of handwriting samples

    of the students of your class and let''s'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 9
  start_sec: 571.75
  end_sec: 619.92
  text: 'of the students of your class and let''s of the students of your class and
    let''s

    look at this factor which is neatness. look at this factor which is neatness.
    look at this factor which is neatness.

    Okay. Now there are going to be some Okay. Now there are going to be some Okay.
    Now there are going to be some

    students who are going to be very neat. students who are going to be very neat.
    students who are going to be very neat.

    Right? They have a handwriting which Right? They have a handwriting which Right?
    They have a handwriting which

    looks almost perfect. There will be some looks almost perfect. There will be some
    looks almost perfect. There will be some

    students whose handwriting is very bad. students whose handwriting is very bad.
    students whose handwriting is very bad.

    You cannot read anything that they have You cannot read anything that they have
    You cannot read anything that they have

    written. And from my class in school, I written. And from my class in school,
    I written. And from my class in school, I

    know that there are these types of know that there are these types of know that
    there are these types of

    people. But most of the people lie in people. But most of the people lie in people.
    But most of the people lie in

    the average. They have a decent the average. They have a decent the average. They
    have a decent

    handwriting which is which can be called handwriting which is which can be called
    handwriting which is which can be called

    as an average handwriting. as an average handwriting. as an average handwriting.

    And this is true for most of the cases And this is true for most of the cases
    And this is true for most of the cases

    that underly uh or that govern the that underly uh or that govern the that underly
    uh or that govern the

    distribution of data that we see in real distribution of data that we see in real
    distribution of data that we see in real

    life. life. life.

    So this is I think very specific to So this is I think very specific to So this
    is I think very specific to

    distributions that you see in in reality distributions that you see in in reality'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 10
  start_sec: 619.92
  end_sec: 679.509
  text: 'distributions that you see in in reality

    and that''s what people try to capture and that''s what people try to capture
    and that''s what people try to capture

    over here. over here. over here.

    So mathematically the regularization So mathematically the regularization So mathematically
    the regularization

    term is denoted by this. We try to term is denoted by this. We try to term is
    denoted by this. We try to

    minimize the kale divergence between minimize the kale divergence between minimize
    the kale divergence between

    the distribution predicted by the the distribution predicted by the the distribution
    predicted by the

    encoder encoder encoder

    and this is a standard gshian and this is a standard gshian and this is a standard
    gshian

    distribution. distribution.

    So you try to move the distribution So you try to move the distribution So you
    try to move the distribution

    which the encoder predicts distribution which the encoder predicts distribution
    which the encoder predicts distribution

    of the latent variables so that it is of the latent variables so that it is of
    the latent variables so that it is

    compressed in that gshian space. You compressed in that gshian space. You compressed
    in that gshian space. You

    don''t you don''t want it to scatter don''t you don''t want it to scatter don''t
    you don''t want it to scatter

    around. [snorts] In reality it will around. [snorts] In reality it will around.
    [snorts] In reality it will

    scatter around. you won''t be able to fit scatter around. you won''t be able to
    fit scatter around. you won''t be able to fit

    it within a perfect ocean. It''s it within a perfect ocean. It''s it within a
    perfect ocean. It''s

    unrealistic I think to do that. But then unrealistic I think to do that. But then
    unrealistic I think to do that. But then

    we try to move it as close as possible. we try to move it as close as possible.
    we try to move it as close as possible.

    I just want you to take a look at this I just want you to take a look at this
    I just want you to take a look at this

    video uh one more time so that we really video uh one more time so that we really
    video uh one more time so that we really

    understand uh the two types of losses'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 11
  start_sec: 679.509
  end_sec: 747.59
  text: 'understand uh the two types of losses understand uh the two types of losses

    which we are encountering here. Okay. So, uh the lower bound is called Okay. So,
    uh the lower bound is called

    as elbow which is also known as the as elbow which is also known as the as elbow
    which is also known as the

    evidence lower bound. evidence lower bound. evidence lower bound.

    So, uh let''s let''s first go through this So, uh let''s let''s first go through
    this So, uh let''s let''s first go through this

    video. So, what we want to do is we want video. So, what we want to do is we want
    video. So, what we want to do is we want

    to teleport a cat from Earth to Mars. to teleport a cat from Earth to Mars. to
    teleport a cat from Earth to Mars.

    And we can''t just teleport every single And we can''t just teleport every single
    And we can''t just teleport every single

    atom in the CAD. It''s it''s a lot of atom in the CAD. It''s it''s a lot of atom
    in the CAD. It''s it''s a lot of

    data. So then what we do is we have a data. So then what we do is we have a data.
    So then what we do is we have a

    Latin code or a recipe where we preserve Latin code or a recipe where we preserve
    Latin code or a recipe where we preserve

    all the important information in this all the important information in this all
    the important information in this

    Latin code and then we transfer this Latin code and then we transfer this Latin
    code and then we transfer this

    Latin code to Mars. Latin code to Mars. Latin code to Mars.

    Now the objective is to maximize the Now the objective is to maximize the Now
    the objective is to maximize the

    likelihood of the data which is likelihood of the data which is likelihood of
    the data which is

    generated by your decoder which is generated by your decoder which is generated
    by your decoder which is

    denoted by P of X. But it turns out that denoted by P of X. But it turns out that
    denoted by P of X. But it turns out that

    P of X is not possible to calculate.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 12
  start_sec: 747.59
  end_sec: 804.959
  text: 'P of X is not possible to calculate. P of X is not possible to calculate.

    It''s intractable It''s intractable It''s intractable

    because you need to calculate an because you need to calculate an because you
    need to calculate an

    integral which is hard to calculate. And integral which is hard to calculate.
    And integral which is hard to calculate. And

    that''s why you find a that''s why you find a that''s why you find a

    parameter or a term which always lies parameter or a term which always lies parameter
    or a term which always lies

    below the true evidence. below the true evidence. below the true evidence.

    And if you maximize this term, you know And if you maximize this term, you know
    And if you maximize this term, you know

    that since it always lies below the true that since it always lies below the true
    that since it always lies below the true

    evidence, your true evidence is going to evidence, your true evidence is going
    to evidence, your true evidence is going to

    be above it. Right? So that''s called as be above it. Right? So that''s called
    as be above it. Right? So that''s called as

    evidence lower bound or elbow. And as I evidence lower bound or elbow. And as
    I evidence lower bound or elbow. And as I

    said, elbow is decomposed into two said, elbow is decomposed into two said, elbow
    is decomposed into two

    terms. The reconstruction loss and the terms. The reconstruction loss and the
    terms. The reconstruction loss and the

    regularization loss. So reconstruction regularization loss. So reconstruction
    regularization loss. So reconstruction

    loss basically says that does the cat loss basically says that does the cat loss
    basically says that does the cat

    which is exported to Mars, does it look which is exported to Mars, does it look
    which is exported to Mars, does it look

    all right? Does it look similar to the all right? Does it look similar to the
    all right? Does it look similar to the

    cat which we have on earth or not? cat which we have on earth or not? cat which
    we have on earth or not?

    And the regularization terms basically And the regularization terms basically
    And the regularization terms basically

    say that is the recipe written in say that is the recipe written in'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 13
  start_sec: 804.959
  end_sec: 874.8
  text: 'say that is the recipe written in

    standard language. Does it follow a standard language. Does it follow a standard
    language. Does it follow a

    distribution which is shown in yellow? distribution which is shown in yellow?
    distribution which is shown in yellow?

    If it does not then we want our recipe If it does not then we want our recipe
    If it does not then we want our recipe

    to match the yellow distribution as to match the yellow distribution as to match
    the yellow distribution as

    close as possible. So you can see we close as possible. So you can see we close
    as possible. So you can see we

    kind of try to make sure the purple kind of try to make sure the purple kind of
    try to make sure the purple

    graph falls on the yellow graph as the graph falls on the yellow graph as the
    graph falls on the yellow graph as the

    training proceeds. training proceeds. training proceeds.

    And we looked at an example where uh we And we looked at an example where uh we
    And we looked at an example where uh we

    actually did this same thing for actually did this same thing for actually did
    this same thing for

    uh reconstructing handwritten digits. And finally we uh here you can see how And
    finally we uh here you can see how

    the latin space uh evolves. the latin space uh evolves. the latin space uh evolves.

    starts from random and it then tries to starts from random and it then tries to
    starts from random and it then tries to

    you know center it around zero with a you know center it around zero with a you
    know center it around zero with a

    variance of one and the quality of the variance of one and the quality of the
    variance of one and the quality of the

    reconstruction looks like this. So something which is very common in So something
    which is very common in

    variational autoenccoders is that the variational autoenccoders is that the variational
    autoenccoders is that the

    reconstructed images appear blurred reconstructed images appear blurred reconstructed
    images appear blurred

    compared to the original images. compared to the original images. compared to
    the original images.

    And this is something we can clearly see And this is something we can clearly
    see'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 14
  start_sec: 874.8
  end_sec: 933.509
  text: 'And this is something we can clearly see

    from this image as well. Every single from this image as well. Every single from
    this image as well. Every single

    output image appears blur compared to output image appears blur compared to output
    image appears blur compared to

    the original image. the original image. the original image.

    And the the same is true if you sample And the the same is true if you sample
    And the the same is true if you sample

    from this 2D Latin space. You can see from this 2D Latin space. You can see from
    this 2D Latin space. You can see

    that vaguely it''s trying to represent that vaguely it''s trying to represent
    that vaguely it''s trying to represent

    the handwritten digits but it is still a the handwritten digits but it is still
    a the handwritten digits but it is still a

    little bit vague. little bit vague. little bit vague.

    So that is the drawback of standard So that is the drawback of standard So that
    is the drawback of standard

    variation autoenccoder that it often variation autoenccoder that it often variation
    autoenccoder that it often

    produces blurry outputs. produces blurry outputs. produces blurry outputs.

    And And And

    another uh major drawback is that the another uh major drawback is that the another
    uh major drawback is that the

    encoder and the decoder have to be encoder and the decoder have to be encoder
    and the decoder have to be

    trained jointly. trained jointly. trained jointly.

    Like you saw in this diagram, we have an Like you saw in this diagram, we have
    an Like you saw in this diagram, we have an

    encoder and we have a decoder, right? encoder and we have a decoder, right? encoder
    and we have a decoder, right?

    And remember we have two kinds of And remember we have two kinds of And remember
    we have two kinds of

    losses. the reconstruction loss and the losses. the reconstruction loss and the
    losses. the reconstruction loss and the

    regularization loss. So the regularization loss. So the regularization loss. So
    the

    regularization loss is linked to the regularization loss is linked to the regularization
    loss is linked to the

    encoder and the reconstruction loss is encoder and the reconstruction loss is
    encoder and the reconstruction loss is

    linked to the decoder which means that'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 15
  start_sec: 933.509
  end_sec: 995.99
  text: 'linked to the decoder which means that linked to the decoder which means
    that

    we have to train two neural networks in we have to train two neural networks in
    we have to train two neural networks in

    this case. One neural network is trained this case. One neural network is trained
    this case. One neural network is trained

    to make sure that the latin space to make sure that the latin space to make sure
    that the latin space

    appears gshian and the second neural appears gshian and the second neural appears
    gshian and the second neural

    network is trained to say that the network is trained to say that the network
    is trained to say that the

    reconstructed image looks as close as reconstructed image looks as close as reconstructed
    image looks as close as

    possible to the original image. So we possible to the original image. So we possible
    to the original image. So we

    have to train two networks at the same have to train two networks at the same
    have to train two networks at the same

    time. into neural networks time. into neural networks time. into neural networks

    and this is something which has and this is something which has and this is something
    which has

    proven to be uh problematic in practical proven to be uh problematic in practical
    proven to be uh problematic in practical

    use cases use cases use cases

    along with the issue that variational along with the issue that variational along
    with the issue that variational

    autoenccoders often produce blurry autoenccoders often produce blurry autoenccoders
    often produce blurry

    images. images. images.

    So with this uh introduction in mind we So with this uh introduction in mind we
    So with this uh introduction in mind we

    are going to move to diffusion modeling are going to move to diffusion modeling
    are going to move to diffusion modeling

    in this lecture in this lecture in this lecture

    and the title of this lecture is and the title of this lecture is and the title
    of this lecture is

    denoising denoising denoising

    diffusion probabilistic models. diffusion probabilistic models. diffusion probabilistic
    models.

    So this was a paper which came out in So this was a paper which came out in So
    this was a paper which came out in

    2020 2020 2020

    which you can see over here denoising'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 16
  start_sec: 995.99
  end_sec: 1062.72
  text: 'which you can see over here denoising which you can see over here denoising

    diffusion probabilistic models diffusion probabilistic models diffusion probabilistic
    models

    and this paper has over and this paper has over and this paper has over

    30 citation uh 30,000 citations if if 30 citation uh 30,000 citations if if 30
    citation uh 30,000 citations if if

    I''m not wrong yeah 32,000 citations I''m not wrong yeah 32,000 citations I''m
    not wrong yeah 32,000 citations

    it is an incredibly popular paper and it is an incredibly popular paper and it
    is an incredibly popular paper and

    it gave a new direction to the field of it gave a new direction to the field of
    it gave a new direction to the field of

    image generation image generation image generation

    and this was the paper which and this was the paper which and this was the paper
    which

    was at the heart of creating a was at the heart of creating a was at the heart
    of creating a

    revolution in image generation using AI revolution in image generation using AI
    revolution in image generation using AI

    and you saw a lot of different uh models and you saw a lot of different uh models
    and you saw a lot of different uh models

    like stable diffusion do incredibly well like stable diffusion do incredibly well
    like stable diffusion do incredibly well

    in generating realistic images in generating realistic images in generating realistic
    images

    and uh the the beauty of this paper is and uh the the beauty of this paper is
    and uh the the beauty of this paper is

    that it laid down a framework that it laid down a framework that it laid down
    a framework

    which gave which gave which gave

    steps which are straightforward steps which are straightforward steps which are
    straightforward

    and it also linked some of the prior and it also linked some of the prior and
    it also linked some of the prior

    works together. So it gave a framework works together. So it gave a framework
    works together. So it gave a framework

    which was coherent with some of the which was coherent with some of the which
    was coherent with some of the

    works which people had done before in works which people had done before in works
    which people had done before in

    literature. literature.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 17
  start_sec: 1062.72
  end_sec: 1116.559
  text: 'literature.

    So diffusion models existed before as So diffusion models existed before as So
    diffusion models existed before as

    well but people had not proven that they well but people had not proven that they
    well but people had not proven that they

    could be used to generate realistic could be used to generate realistic could
    be used to generate realistic

    images and this paper images and this paper images and this paper

    uh showed that yes it can be used for uh showed that yes it can be used for uh
    showed that yes it can be used for

    that purpose and they laid down a recipe that purpose and they laid down a recipe
    that purpose and they laid down a recipe

    which was which was which was

    practical for researchers to implement practical for researchers to implement
    practical for researchers to implement

    and from there on there was no stopping. and from there on there was no stopping.
    and from there on there was no stopping.

    So we are going to look at uh this paper So we are going to look at uh this paper
    So we are going to look at uh this paper

    in detail. We are going to deconstruct in detail. We are going to deconstruct
    in detail. We are going to deconstruct

    this paper. I want all of you to also this paper. I want all of you to also this
    paper. I want all of you to also

    take a print out of this paper and keep take a print out of this paper and keep
    take a print out of this paper and keep

    it handy. It won''t be required for this it handy. It won''t be required for this
    it handy. It won''t be required for this

    particular lecture. But once we are done particular lecture. But once we are done
    particular lecture. But once we are done

    with this lecture and you go through the with this lecture and you go through
    the with this lecture and you go through the

    lecture material, I think you will have lecture material, I think you will have
    lecture material, I think you will have

    a nice time understanding what the a nice time understanding what the a nice time
    understanding what the

    authors have written. So for that authors have written. So for that'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 18
  start_sec: 1116.559
  end_sec: 1182.39
  text: 'authors have written. So for that

    purpose I would really recommend all of purpose I would really recommend all of
    purpose I would really recommend all of

    you to take a print out and keep it you to take a print out and keep it you to
    take a print out and keep it

    handy. handy. handy.

    Okay. So let''s get started. U this is Okay. So let''s get started. U this is
    Okay. So let''s get started. U this is

    the first time that we are using the the first time that we are using the the
    first time that we are using the

    word diffusion in this series and uh I have not really and uh I have not really

    use this word before. use this word before. use this word before.

    So when I first came across the word So when I first came across the word So when
    I first came across the word

    diffusion, it diffusion, it diffusion, it

    took my mind to the the area of physics. took my mind to the the area of physics.
    took my mind to the the area of physics.

    I had learned diffusion techniques or I had learned diffusion techniques or I
    had learned diffusion techniques or

    the principles of diffusion in my the principles of diffusion in my the principles
    of diffusion in my

    college where it meant that diffusion is college where it meant that diffusion
    is college where it meant that diffusion is

    a tendency of particles to a tendency of particles to a tendency of particles
    to

    move and spread out until they are move and spread out until they are move and
    spread out until they are

    evenly distributed. evenly distributed. evenly distributed.

    So for example, if we take an example of So for example, if we take an example
    of So for example, if we take an example of

    perfume, if let''s say I apply perfume uh perfume, if let''s say I apply perfume
    uh perfume, if let''s say I apply perfume uh

    and I''m standing in one corner of the and I''m standing in one corner of the
    and I''m standing in one corner of the

    room, the smell slowly percolates to the room, the smell slowly percolates to
    the room, the smell slowly percolates to the

    other corner of the room, right? So it''s'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 19
  start_sec: 1182.39
  end_sec: 1245.6
  text: 'other corner of the room, right? So it''s other corner of the room, right?
    So it''s

    it''s it''s like the it''s it''s like the it''s it''s like the

    particles which are uh particles which are uh particles which are uh

    which are created, they are there, which are created, they are there, which are
    created, they are there,

    they''re they''re moving through space. they''re they''re moving through space.
    they''re they''re moving through space.

    They are moving from one point of space They are moving from one point of space
    They are moving from one point of space

    and they''re going to another point in and they''re going to another point in
    and they''re going to another point in

    space and this tendency of movement from space and this tendency of movement from
    space and this tendency of movement from

    one area from one locality one area from one locality one area from one locality

    it kind of diffuses so it kind of moves it kind of diffuses so it kind of moves
    it kind of diffuses so it kind of moves

    out and and makes it even. out and and makes it even. out and and makes it even.

    Another example is sugar dissolving and Another example is sugar dissolving and
    Another example is sugar dissolving and

    spreading uniformly in water. spreading uniformly in water. spreading uniformly
    in water.

    So you can see how how So you can see how how So you can see how how

    it it''s it''s localized in the beginning it it''s it''s localized in the beginning
    it it''s it''s localized in the beginning

    at the bottom of the mug and then as you at the bottom of the mug and then as
    you at the bottom of the mug and then as you

    stir it the particles move out and then stir it the particles move out and then
    stir it the particles move out and then

    you get a uniform color. [snorts] you get a uniform color. [snorts] you get a
    uniform color. [snorts]

    So this was my idea of of of diffusion So this was my idea of of of diffusion
    So this was my idea of of of diffusion

    and to apply this technique to the field and to apply this technique to the field
    and to apply this technique to the field

    of artificial intelligence. of artificial intelligence.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 20
  start_sec: 1245.6
  end_sec: 1304.31
  text: 'of artificial intelligence.

    It sounded It sounded It sounded

    like ridiculous because how how can you like ridiculous because how how can you
    like ridiculous because how how can you

    apply this to AI, right? apply this to AI, right? apply this to AI, right?

    But then there are some properties which But then there are some properties which
    But then there are some properties which

    diffusion processes carry which we diffusion processes carry which we diffusion
    processes carry which we

    should note down at the beginning is should note down at the beginning is should
    note down at the beginning is

    that the structure slowly disappears. that the structure slowly disappears. that
    the structure slowly disappears.

    This is the first point This is the first point This is the first point

    and the second point is that things and the second point is that things and the
    second point is that things

    become uniform and noisy over time. become uniform and noisy over time. become
    uniform and noisy over time.

    So you [snorts] can see initially there So you [snorts] can see initially there
    So you [snorts] can see initially there

    was a structure to this sugar right? It was a structure to this sugar right? It
    was a structure to this sugar right? It

    kind of settled at the bottom of this kind of settled at the bottom of this kind
    of settled at the bottom of this

    cup and then as you stirred it, it cup and then as you stirred it, it cup and
    then as you stirred it, it

    became uniform. The structure became uniform. The structure became uniform. The
    structure

    disappeared. So it''s almost like you disappeared. So it''s almost like you disappeared.
    So it''s almost like you

    created noise from the original settled created noise from the original settled
    created noise from the original settled

    sugar at the bottom image. sugar at the bottom image. sugar at the bottom image.

    Okay. So uh this is what we understand Okay. So uh this is what we understand
    Okay. So uh this is what we understand

    by diffusion and now we are going to by diffusion and now we are going to by diffusion
    and now we are going to

    link it to link it to link it to

    AI and uh we are going to see how the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 21
  start_sec: 1304.31
  end_sec: 1363.76
  text: 'AI and uh we are going to see how the AI and uh we are going to see how the

    diffusion technique is used for diffusion technique is used for diffusion technique
    is used for

    reproducing the original data reproducing the original data reproducing the original
    data

    distribution. Remember the whole thing distribution. Remember the whole thing
    distribution. Remember the whole thing

    that we started out was deep generative that we started out was deep generative
    that we started out was deep generative

    modeling which was that we are given a modeling which was that we are given a
    modeling which was that we are given a

    true data distribution which we have no true data distribution which we have no
    true data distribution which we have no

    idea what the data distribution is but idea what the data distribution is but
    idea what the data distribution is but

    we want to sample from that data we want to sample from that data we want to sample
    from that data

    distribution without having no idea what distribution without having no idea what
    distribution without having no idea what

    that data distribution is. So then that data distribution is. So then that data
    distribution is. So then

    [snorts] we want some way to predict the [snorts] we want some way to predict
    the [snorts] we want some way to predict the

    true data distribution and then sample true data distribution and then sample
    true data distribution and then sample

    from it. And from it. And from it. And

    the the first method that we saw was VAS the the first method that we saw was
    VAS the the first method that we saw was VAS

    which did predict this distribution but which did predict this distribution but
    which did predict this distribution but

    it had a lot of challenges as we saw it had a lot of challenges as we saw it had
    a lot of challenges as we saw

    before. Okay. So u Okay. So u

    the the main question is that can we do the the main question is that can we do
    the the main question is that can we do

    something similar with our data as well? something similar with our data as well?
    something similar with our data as well?

    That''s what we are going to think about That''s what we are going to think about'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 22
  start_sec: 1363.76
  end_sec: 1436.07
  text: 'That''s what we are going to think about

    because our primary intention is to because our primary intention is to because
    our primary intention is to

    reproduce the original or the true data reproduce the original or the true data
    reproduce the original or the true data

    distribution. distribution.

    So if we want to use diffusion, if you So if we want to use diffusion, if you
    So if we want to use diffusion, if you

    want to use the method of diffusion, it want to use the method of diffusion, it
    want to use the method of diffusion, it

    makes sense to apply this method to our makes sense to apply this method to our
    makes sense to apply this method to our

    data. So remember that in the variational So remember that in the variational

    autoenccoder our encoder took the data autoenccoder our encoder took the data
    autoenccoder our encoder took the data

    as an input like you see over here as an input like you see over here as an input
    like you see over here

    and and and

    it converted the data to some areas in it converted the data to some areas in
    it converted the data to some areas in

    the latent space like this. Okay. So the data is converted into a Okay. So the
    data is converted into a

    compact representation. compact representation. compact representation.

    [snorts] [snorts] [snorts]

    Now uh the first thing that comes to my Now uh the first thing that comes to my
    Now uh the first thing that comes to my

    mind when someone says apply the method mind when someone says apply the method
    mind when someone says apply the method

    of diffusion to data is can we just of diffusion to data is can we just of diffusion
    to data is can we just

    replace this with a diffuser. replace this with a diffuser. replace this with
    a diffuser.

    So what if we think of our encoder as a So what if we think of our encoder as
    a So what if we think of our encoder as a

    machine which diffuses the data machine which diffuses the data machine which
    diffuses the data

    and by diffuses I mean makes the data and by diffuses I mean makes the data and
    by diffuses I mean makes the data

    uniform and noisy removes all the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 23
  start_sec: 1436.07
  end_sec: 1498.72
  text: 'uniform and noisy removes all the uniform and noisy removes all the

    structure in the data. structure in the data. structure in the data.

    What if we think of our encoder as being What if we think of our encoder as being
    What if we think of our encoder as being

    repurposed for that purpose and we''ll repurposed for that purpose and we''ll
    repurposed for that purpose and we''ll

    call it a diffuser. [snorts] call it a diffuser. [snorts] call it a diffuser.
    [snorts]

    So u okay so by looking at this parallel So u okay so by looking at this parallel
    So u okay so by looking at this parallel

    between diffusion of particles and between diffusion of particles and between
    diffusion of particles and

    diffusion of images diffusion of images diffusion of images

    what if we consider each pixel in the what if we consider each pixel in the what
    if we consider each pixel in the

    image as a particle image as a particle image as a particle

    and by the process of diffusion we want and by the process of diffusion we want
    and by the process of diffusion we want

    this pixel to lose all the information this pixel to lose all the information
    this pixel to lose all the information

    and just become noise and just become noise and just become noise

    basically lose all the data that that basically lose all the data that that basically
    lose all the data that that

    that that this pixel has. that that this pixel has. that that this pixel has.

    Okay. So, let''s let''s take an example. Okay. So, let''s let''s take an example.
    Okay. So, let''s let''s take an example.

    Uh we want to take an example of Batman Uh we want to take an example of Batman
    Uh we want to take an example of Batman

    and uh we want to convert this image of and uh we want to convert this image of
    and uh we want to convert this image of

    Batman into pure noise. By pure noise, I Batman into pure noise. By pure noise,
    I Batman into pure noise. By pure noise, I

    mean I want the entire structure to mean I want the entire structure to mean I
    want the entire structure to

    disappear. When people look at the final disappear. When people look at the final'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 24
  start_sec: 1498.72
  end_sec: 1558.23
  text: 'disappear. When people look at the final

    image, they have no idea that this came image, they have no idea that this came
    image, they have no idea that this came

    from Batman. This could have this this from Batman. This could have this this
    from Batman. This could have this this

    this could have come from any image on this could have come from any image on
    this could have come from any image on

    the internet. the internet. the internet.

    So the encoder will do something like So the encoder will do something like So
    the encoder will do something like

    this. The encoder will take this image this. The encoder will take this image
    this. The encoder will take this image

    and then convert it into complete noise. and then convert it into complete noise.
    and then convert it into complete noise.

    Okay, this is what we want to achieve. Okay, this is what we want to achieve.
    Okay, this is what we want to achieve.

    We want to go from the image on the left We want to go from the image on the left
    We want to go from the image on the left

    and we want to reach the image on the and we want to reach the image on the and
    we want to reach the image on the

    right. [snorts] right. [snorts] right. [snorts]

    The question is how do we make this The question is how do we make this The question
    is how do we make this

    jump? jump? jump?

    How do we remove the structure in this How do we remove the structure in this
    How do we remove the structure in this

    data and how do we data and how do we data and how do we

    transform it to noise? Uh just think about it before we go Uh just think about
    it before we go

    ahead. ahead. ahead.

    We will make one additional change. We will make one additional change. We will
    make one additional change.

    Instead of directly transforming this Instead of directly transforming this Instead
    of directly transforming this

    image, uh we will transform it image, uh we will transform it image, uh we will
    transform it

    gradually. We''ll transform it step by gradually. We''ll transform it step by
    gradually. We''ll transform it step by

    step. First we will add some noise. Then'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 25
  start_sec: 1558.23
  end_sec: 1619.2
  text: 'step. First we will add some noise. Then step. First we will add some noise.
    Then

    we''ll add another noise and then slowly we''ll add another noise and then slowly
    we''ll add another noise and then slowly

    and steadily the structure will and steadily the structure will and steadily the
    structure will

    disappear. So in this particular flow disappear. So in this particular flow disappear.
    So in this particular flow

    you can see that I have used four you can see that I have used four you can see
    that I have used four

    diffusers 1 2 3 and four diffusers 1 2 3 and four diffusers 1 2 3 and four

    which means that are there multiple which means that are there multiple which
    means that are there multiple

    encoders to be trained. encoders to be trained. encoders to be trained.

    So remember this was a major drawback of So remember this was a major drawback
    of So remember this was a major drawback of

    VAES where both encoder and decoder had VAES where both encoder and decoder had
    VAES where both encoder and decoder had

    to be trained simultaneously. to be trained simultaneously. to be trained simultaneously.

    [snorts] One of the biggest [snorts] One of the biggest [snorts] One of the biggest

    contributions of the DDPM paper is this. contributions of the DDPM paper is this.
    contributions of the DDPM paper is this.

    They asked this question that what if we They asked this question that what if
    we They asked this question that what if we

    fix the encoder distribution? fix the encoder distribution? fix the encoder distribution?

    What if we don''t What if we don''t What if we don''t

    uh uh uh

    make it like a learnable encoder but we make it like a learnable encoder but we
    make it like a learnable encoder but we

    have a fixed encoder which transforms have a fixed encoder which transforms have
    a fixed encoder which transforms

    the data to pure noise the data to pure noise the data to pure noise

    and every single image can be and every single image can be and every single image
    can be

    transformed into pure noise. Let''s say I transformed into pure noise. Let''s
    say I transformed into pure noise. Let''s say I

    am holding this bottle in front of me. I am holding this bottle in front of me.
    I'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 26
  start_sec: 1619.2
  end_sec: 1672.96
  text: 'am holding this bottle in front of me. I

    take an image of this and I want take an image of this and I want take an image
    of this and I want

    something which can transform this image something which can transform this image
    something which can transform this image

    to noise. So when you look at noise, it to noise. So when you look at noise, it
    to noise. So when you look at noise, it

    could have come from anywhere. But right could have come from anywhere. But right
    could have come from anywhere. But right

    now we are looking at just the encoder now we are looking at just the encoder
    now we are looking at just the encoder

    and we want to fix this transition. So and we want to fix this transition. So
    and we want to fix this transition. So

    how could I change every pixel so that how could I change every pixel so that
    how could I change every pixel so that

    it becomes noise? it becomes noise? it becomes noise?

    What does noise mean? What does noise mean? What does noise mean?

    Let''s let''s understand this. So, uh we Let''s let''s understand this. So, uh
    we Let''s let''s understand this. So, uh we

    will add a fixed gshian kernel to this will add a fixed gshian kernel to this
    will add a fixed gshian kernel to this

    image. image. image.

    [snorts] [snorts]

    I I''ll I''ll unpack this. Uh so, don''t I I''ll I''ll unpack this. Uh so, don''t
    I I''ll I''ll unpack this. Uh so, don''t

    don''t don''t worry about it. We''ll we''ll don''t don''t worry about it. We''ll
    we''ll don''t don''t worry about it. We''ll we''ll

    try to understand what does a gshian try to understand what does a gshian try
    to understand what does a gshian

    kernel mean. kernel mean. kernel mean.

    The first step that we will do is we The first step that we will do is we The
    first step that we will do is we

    will divide uh this will divide uh this will divide uh this

    image of Batman into pixels. So, you can image of Batman into pixels. So, you
    can image of Batman into pixels. So, you can

    see all of these individual grids. They see all of these individual grids. They'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 27
  start_sec: 1672.96
  end_sec: 1758.64
  text: 'see all of these individual grids. They

    are one one pixel each and every single are one one pixel each and every single
    are one one pixel each and every single

    pixel holds some value. For example, pixel holds some value. For example, pixel
    holds some value. For example,

    this pixel here which is pixel number this pixel here which is pixel number this
    pixel here which is pixel number

    one, one, one,

    it holds a value of 0.5. Pixel number it holds a value of 0.5. Pixel number it
    holds a value of 0.5. Pixel number

    two holds another holds a value of 0.5. two holds another holds a value of 0.5.
    two holds another holds a value of 0.5.

    I''m considering only one channel here. I''m considering only one channel here.
    I''m considering only one channel here.

    So ignore the So ignore the So ignore the

    u variation which can happen if we have u variation which can happen if we have
    u variation which can happen if we have

    three channels like RGB. three channels like RGB. three channels like RGB.

    Okay. So every pixel holds certain Okay. So every pixel holds certain Okay. So
    every pixel holds certain

    value. Now what does it mean by adding value. Now what does it mean by adding
    value. Now what does it mean by adding

    noise to this pixel? What I do is I noise to this pixel? What I do is I noise
    to this pixel? What I do is I

    create a gshian distribution. create a gshian distribution. create a gshian distribution.

    So this this value is 0.5 right? So I So this this value is 0.5 right? So I So
    this this value is 0.5 right? So I

    create a gshian distribution which is create a gshian distribution which is create
    a gshian distribution which is

    centered at 0.5 and having a small deviation of beta. and having a small deviation
    of beta.

    So this deviation is standard deviation So this deviation is standard deviation
    So this deviation is standard deviation

    which is called as beta. And I will sample from this gshian And I will sample
    from this gshian

    distribution. Okay. So, now this as I sample from this Okay. So, now this as I
    sample from this

    obviously the value is not going to be obviously the value is not going to be'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 28
  start_sec: 1758.64
  end_sec: 1803.99
  text: 'obviously the value is not going to be

    0.5. The value is going to be different 0.5. The value is going to be different
    0.5. The value is going to be different

    than 0.5. It''s either going to be than 0.5. It''s either going to be than 0.5.
    It''s either going to be

    greater than 0.5 or it''s going to be greater than 0.5 or it''s going to be greater
    than 0.5 or it''s going to be

    less than 0.5. less than 0.5. less than 0.5.

    And this is exactly what we mean by And this is exactly what we mean by And this
    is exactly what we mean by

    adding noise. We are changing the value adding noise. We are changing the value
    adding noise. We are changing the value

    of the pixel itself. Now, this is also of the pixel itself. Now, this is also
    of the pixel itself. Now, this is also

    given here. We have a gshian curve which given here. We have a gshian curve which
    given here. We have a gshian curve which

    is centered at the mean and with a is centered at the mean and with a is centered
    at the mean and with a

    standard deviation of beta 1. So we standard deviation of beta 1. So we standard
    deviation of beta 1. So we

    sample from this. sample from this. sample from this.

    And the main idea is that we don''t just And the main idea is that we don''t just
    And the main idea is that we don''t just

    do this for one pixel but we do it for do this for one pixel but we do it for
    do this for one pixel but we do it for

    every single pixel in this image. Now if every single pixel in this image. Now
    if every single pixel in this image. Now if

    we consider this pixel this pixel has a we consider this pixel this pixel has
    a we consider this pixel this pixel has a

    value of 0.1. So the goshian curve will value of 0.1. So the goshian curve will
    value of 0.1. So the goshian curve will

    be centered at 0.1 but then it will have be centered at 0.1 but then it will have
    be centered at 0.1 but then it will have

    the same deviation of of beta 1. and'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 29
  start_sec: 1803.99
  end_sec: 1866.549
  text: 'the same deviation of of beta 1. and the same deviation of of beta 1. and

    then we''ll again sample from it. then we''ll again sample from it. then we''ll
    again sample from it.

    So we will continue to do this for every So we will continue to do this for every
    So we will continue to do this for every

    single pixel in the image. single pixel in the image. single pixel in the image.

    So there are let''s say 784 pixels in So there are let''s say 784 pixels in So
    there are let''s say 784 pixels in

    this image because I have divided it this image because I have divided it this
    image because I have divided it

    into 28 rows and 28 columns. So for into 28 rows and 28 columns. So for into 28
    rows and 28 columns. So for

    every single pixel of out of 784 I will every single pixel of out of 784 I will
    every single pixel of out of 784 I will

    add noise which means that I will sample add noise which means that I will sample
    add noise which means that I will sample

    from a gshian which is centered at the from a gshian which is centered at the
    from a gshian which is centered at the

    mean and have a standard deviation of mean and have a standard deviation of mean
    and have a standard deviation of

    beta. So this standard deviation is what beta. So this standard deviation is what
    beta. So this standard deviation is what

    causes the noise or adds the noise to causes the noise or adds the noise to causes
    the noise or adds the noise to

    the pixel. Now intuitively what do you think will Now intuitively what do you
    think will

    happen if we do this for all the pixels happen if we do this for all the pixels
    happen if we do this for all the pixels

    in the image? in the image? in the image?

    How will this image transform? How how How will this image transform? How how
    How will this image transform? How how

    will the transformed image really look will the transformed image really look
    will the transformed image really look

    like? So the transformed image looks like So the transformed image looks like

    this. You can see that it''s not'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 30
  start_sec: 1866.549
  end_sec: 1927.6
  text: 'this. You can see that it''s not this. You can see that it''s not

    completely noise but it''s becoming completely noise but it''s becoming completely
    noise but it''s becoming

    noisier, right? It''s it''s slowly noisier, right? It''s it''s slowly noisier,
    right? It''s it''s slowly

    becoming noisier. [snorts] becoming noisier. [snorts] becoming noisier. [snorts]

    And this you have only done for one And this you have only done for one And this
    you have only done for one

    diffuser. diffuser. diffuser.

    Now the question is I want to do this Now the question is I want to do this Now
    the question is I want to do this

    again and again and again till it again and again and again till it again and
    again and again till it

    becomes complete noise. becomes complete noise. becomes complete noise.

    So let''s say I do it a large number of So let''s say I do it a large number of
    So let''s say I do it a large number of

    times and uh I I get something like times and uh I I get something like times
    and uh I I get something like

    this. Notice how the noise is gradually being Notice how the noise is gradually
    being

    added to this image and and the pixel intensity actually and and the pixel intensity
    actually

    changes. It it drops down in this case. changes. It it drops down in this case.
    changes. It it drops down in this case.

    >> [sighs and snorts] >> [sighs and snorts] >> [sighs and snorts]

    >> which which also makes sense because >> which which also makes sense because
    >> which which also makes sense because

    every pixel is undergoing a major every pixel is undergoing a major every pixel
    is undergoing a major

    transformation. This is first you get a transformation. This is first you get
    a transformation. This is first you get a

    sample from this then you take a sample sample from this then you take a sample
    sample from this then you take a sample

    from that sample then you again take a from that sample then you again take a
    from that sample then you again take a

    sample from that in the next sample from that in the next sample from that in
    the next

    gshian transition kernel and you do it gshian transition kernel and you do it'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 31
  start_sec: 1927.6
  end_sec: 1996.63
  text: 'gshian transition kernel and you do it

    several times. several times. several times.

    So this is the process which is called So this is the process which is called
    So this is the process which is called

    as transforming an image using a gshian as transforming an image using a gshian
    as transforming an image using a gshian

    transition kernel. But have we obtained what we set out to But have we obtained
    what we set out to

    obtain? Let''s try to understand what our obtain? Let''s try to understand what
    our obtain? Let''s try to understand what our

    intuition was. intuition was. intuition was.

    We want the structure to slowly We want the structure to slowly We want the structure
    to slowly

    disappear and we want things to become disappear and we want things to become
    disappear and we want things to become

    uniform and noisy over time. uniform and noisy over time. uniform and noisy over
    time.

    The problem with this is that you do get The problem with this is that you do
    get The problem with this is that you do get

    some noisy structure but the structure some noisy structure but the structure
    some noisy structure but the structure

    is not exactly disappearing. I can still is not exactly disappearing. I can still
    is not exactly disappearing. I can still

    tell that this is the Batman. tell that this is the Batman. tell that this is
    the Batman.

    Right? Right? Right?

    So the main change that we have to do So the main change that we have to do So
    the main change that we have to do

    or the the reason why it doesn''t the or the the reason why it doesn''t the or
    the the reason why it doesn''t the

    structure doesn''t completely disappear. structure doesn''t completely disappear.
    structure doesn''t completely disappear.

    The answer lies in this first The answer lies in this first The answer lies in
    this first

    transformation that you did and we have transformation that you did and we have
    transformation that you did and we have

    to do something different over there. to do something different over there. to
    do something different over there.

    [snorts] [snorts]

    Now what is the different thing that we Now what is the different thing that we
    Now what is the different thing that we

    can do? can do? can do?

    Let''s try to understand.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 32
  start_sec: 1996.63
  end_sec: 2071.829
  text: 'Let''s try to understand. Let''s try to understand.

    Remember that we are preserving the mean Remember that we are preserving the mean
    Remember that we are preserving the mean

    value of the pixels. The mean of the value of the pixels. The mean of the value
    of the pixels. The mean of the

    gshian gshian gshian

    [snorts] is the same as the value of [snorts] is the same as the value of [snorts]
    is the same as the value of

    these pixels. these pixels. these pixels.

    And that is that is where we are And that is that is where we are And that is
    that is where we are

    preserving the structure. This this mean preserving the structure. This this mean
    preserving the structure. This this mean

    remains the same for every transition remains the same for every transition remains
    the same for every transition

    you have the mean which stays the same you have the mean which stays the same
    you have the mean which stays the same

    as the previous value of that pixel. the structure is preserved. the structure
    is preserved.

    Now uh we want the structure to break Now uh we want the structure to break Now
    uh we want the structure to break

    which means that we want the mean to which means that we want the mean to which
    means that we want the mean to

    slowly change and move to zero. slowly change and move to zero. slowly change
    and move to zero.

    Right now the mean is not moving to zero Right now the mean is not moving to zero
    Right now the mean is not moving to zero

    but we want the mean of every single but we want the mean of every single but
    we want the mean of every single

    pixel to slowly move towards zero. pixel to slowly move towards zero. pixel to
    slowly move towards zero.

    So what we do is uh let''s take So what we do is uh let''s take So what we do
    is uh let''s take

    the same pixel number one. For pixel number one, we again sample For pixel number
    one, we again sample

    from a gshian but this time we sample from a gshian but this time we sample from
    a gshian but this time we sample

    from a gshian which with a mean which is'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 33
  start_sec: 2071.829
  end_sec: 2163.99
  text: 'from a gshian which with a mean which is from a gshian which with a mean
    which is

    slightly scaled down from this mean. slightly scaled down from this mean. slightly
    scaled down from this mean.

    So this means that we multiply this mean So this means that we multiply this mean
    So this means that we multiply this mean

    by a factor of alpha. by a factor of alpha. by a factor of alpha.

    So alpha into.5. So let''s say alpha is half. So then this So let''s say alpha
    is half. So then this

    becomes 0.25. So we have a mean now of 0.25. the So we have a mean now of 0.25.
    the

    standard deviation remains the same as standard deviation remains the same as
    standard deviation remains the same as

    beta 1 and now you sample from this and now you sample from this

    distribution. So uh what we do is for every single So uh what we do is for every
    single

    pixel we scale the mean by a factor of pixel we scale the mean by a factor of
    pixel we scale the mean by a factor of

    alpha alpha alpha

    and we add a standard deviation which is and we add a standard deviation which
    is and we add a standard deviation which is

    beta beta beta

    and we do this for every single pixel in and we do this for every single pixel
    in and we do this for every single pixel in

    the image. the image. the image.

    And now let us see what happens if we do And now let us see what happens if we
    do And now let us see what happens if we do

    this for multiple times. this for multiple times. this for multiple times.

    If we do this multiple times, this is If we do this multiple times, this is If
    we do this multiple times, this is

    what we get. This is exactly what we want. The This is exactly what we want. The

    structure becomes uniform and the structure becomes uniform and the structure
    becomes uniform and the

    structure disappears. structure disappears. structure disappears.

    So with a small little change of scaling So with a small little change of scaling
    So with a small little change of scaling

    down the mean, we have made sure that'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 34
  start_sec: 2163.99
  end_sec: 2219.109
  text: 'down the mean, we have made sure that down the mean, we have made sure that

    the mean of every single pixel goes down the mean of every single pixel goes down
    the mean of every single pixel goes down

    for every iteration and that''s why the for every iteration and that''s why the
    for every iteration and that''s why the

    structure disappears and uh you get structure disappears and uh you get structure
    disappears and uh you get

    complete noise at the end of it. So, so this is this is very exciting, So, so
    this is this is very exciting,

    right? And uh this is this is how the right? And uh this is this is how the right?
    And uh this is this is how the

    forward process this is what our encoder forward process this is what our encoder
    forward process this is what our encoder

    is going to do. Now, our encoder is is going to do. Now, our encoder is is going
    to do. Now, our encoder is

    fixed. It''s not like a variational fixed. It''s not like a variational fixed.
    It''s not like a variational

    autoenccoder where it''s a neural network autoenccoder where it''s a neural network
    autoenccoder where it''s a neural network

    which you have to train. But our encoder which you have to train. But our encoder
    which you have to train. But our encoder

    is this gshian kernel which transforms is this gshian kernel which transforms
    is this gshian kernel which transforms

    every image that you show in the data to every image that you show in the data
    to every image that you show in the data to

    noise. That''s all which our encoder is noise. That''s all which our encoder is
    noise. That''s all which our encoder is

    going to do. Let''s say you want to train going to do. Let''s say you want to
    train going to do. Let''s say you want to train

    a diffusion model to predict images of a diffusion model to predict images of
    a diffusion model to predict images of

    bottles. bottles. bottles.

    The encoder will again do the same The encoder will again do the same The encoder
    will again do the same

    thing. It will convert all images of thing. It will convert all images of thing.
    It will convert all images of

    bottles into pure noise.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 35
  start_sec: 2219.109
  end_sec: 2282.64
  text: 'bottles into pure noise. bottles into pure noise.

    And that happens for any data that you And that happens for any data that you
    And that happens for any data that you

    feed into the encoder. feed into the encoder. feed into the encoder.

    So uh So uh So uh

    whoever came up with this idea of whoever came up with this idea of whoever came
    up with this idea of

    transforming images to noise [snorts] transforming images to noise [snorts] transforming
    images to noise [snorts]

    I think that''s I think that''s I think that''s

    a great idea and and and the reason is a great idea and and and the reason is
    a great idea and and and the reason is

    that if if we ask the question that if if we ask the question that if if we ask
    the question

    what does every single image in the what does every single image in the what does
    every single image in the

    world come from? Give me one structure world come from? Give me one structure
    world come from? Give me one structure

    from where I can generate any image. from where I can generate any image. from
    where I can generate any image.

    [snorts] [snorts]

    And this question appears baffling at And this question appears baffling at And
    this question appears baffling at

    first but if you think about it the first but if you think about it the first
    but if you think about it the

    answer is noise. answer is noise. answer is noise.

    The reason is that if you start with The reason is that if you start with The
    reason is that if you start with

    noise by removing the noise noise by removing the noise noise by removing the
    noise

    strategically you can generate any strategically you can generate any strategically
    you can generate any

    single image in the world. single image in the world. single image in the world.

    [snorts] [snorts]

    So it makes sense for our encoder to So it makes sense for our encoder to So it
    makes sense for our encoder to

    encode all the images, encode the data encode all the images, encode the data
    encode all the images, encode the data

    into something into something into something

    from where any image in the world can be from where any image in the world can
    be'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 36
  start_sec: 2282.64
  end_sec: 2331.2
  text: 'from where any image in the world can be

    generated. generated. generated.

    So essentially we are looking at So essentially we are looking at So essentially
    we are looking at

    something which is at the heart of all something which is at the heart of all
    something which is at the heart of all

    the images [snorts] and this is not very the images [snorts] and this is not very
    the images [snorts] and this is not very

    straightforward or very intuitive straightforward or very intuitive straightforward
    or very intuitive

    because every image looks so different, because every image looks so different,
    because every image looks so different,

    right? So how can we generate every right? So how can we generate every right?
    So how can we generate every

    single image back from noise? But that single image back from noise? But that
    single image back from noise? But that

    is exactly what we do in in this paper. is exactly what we do in in this paper.
    is exactly what we do in in this paper.

    We will come to that later. But I I want We will come to that later. But I I want
    We will come to that later. But I I want

    to help you build your intuition with to help you build your intuition with to
    help you build your intuition with

    respect to this topic. respect to this topic. respect to this topic.

    Okay. So now we express this diffusion Okay. So now we express this diffusion
    Okay. So now we express this diffusion

    process as follows. For every pixel in process as follows. For every pixel in
    process as follows. For every pixel in

    the image the image the image

    sample from a gshian distribution, the sample from a gshian distribution, the
    sample from a gshian distribution, the

    mean of the gshian distribution should mean of the gshian distribution should
    mean of the gshian distribution should

    be scaled by a factor of alpha and the be scaled by a factor of alpha and the
    be scaled by a factor of alpha and the

    standard deviation should be beta. standard deviation should be beta. standard
    deviation should be beta.

    >> [snorts] >> [snorts] >> [snorts]

    >> This is given by this. The first image >> This is given by this. The first
    image'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 37
  start_sec: 2331.2
  end_sec: 2388.88
  text: '>> This is given by this. The first image

    I''m going to denote as X0. The second I''m going to denote as X0. The second
    I''m going to denote as X0. The second

    image I''ll denote as X1 and so on. Now image I''ll denote as X1 and so on. Now
    image I''ll denote as X1 and so on. Now

    this transition from X0 to X1 happens this transition from X0 to X1 happens this
    transition from X0 to X1 happens

    because we apply a Gshian distribution because we apply a Gshian distribution
    because we apply a Gshian distribution

    here with a mean scaled scaled by alpha here with a mean scaled scaled by alpha
    here with a mean scaled scaled by alpha

    1 and the standard deviation as beta 1. 1 and the standard deviation as beta 1.
    1 and the standard deviation as beta 1.

    Similarly, we do for the next transition Similarly, we do for the next transition
    Similarly, we do for the next transition

    where we have the mean scaled by alpha 2 where we have the mean scaled by alpha
    2 where we have the mean scaled by alpha 2

    and the standard deviation as beta_2. and the standard deviation as beta_2. and
    the standard deviation as beta_2.

    Here it should be noted that I''m not Here it should be noted that I''m not Here
    it should be noted that I''m not

    using the same alpha and beta using the same alpha and beta using the same alpha
    and beta

    everywhere. I''m using different alpha 1, everywhere. I''m using different alpha
    1, everywhere. I''m using different alpha 1,

    beta 1, alpha 2, beta 2 etc. Now the this is what we do until we Now the this
    is what we do until we

    transform into pure noise. Okay. So so the question is why are we Okay. So so
    the question is why are we

    choosing different betas? Why beta 1, choosing different betas? Why beta 1, choosing
    different betas? Why beta 1,

    beta 2, beta 3, beta 4 etc. beta 2, beta 3, beta 4 etc. beta 2, beta 3, beta 4
    etc.

    So the betas which are chosen they are So the betas which are chosen they are
    So the betas which are chosen they are

    also called as noise schedule. also called as noise schedule.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 38
  start_sec: 2388.88
  end_sec: 2438.88
  text: 'also called as noise schedule.

    So beta is what adds noise to the image. So beta is what adds noise to the image.
    So beta is what adds noise to the image.

    Uh and we have different betas because Uh and we have different betas because
    Uh and we have different betas because

    as we get closer and closer to the noisy as we get closer and closer to the noisy
    as we get closer and closer to the noisy

    image, we want to add more and more image, we want to add more and more image,
    we want to add more and more

    noise. This is something which noise. This is something which noise. This is something
    which

    researchers have found to work well in researchers have found to work well in
    researchers have found to work well in

    practice. And this is a standard noise practice. And this is a standard noise
    practice. And this is a standard noise

    schedule which is used. There is usually schedule which is used. There is usually
    schedule which is used. There is usually

    some some schedule which which ensures some some schedule which which ensures
    some some schedule which which ensures

    that the beta values increase with time. that the beta values increase with time.
    that the beta values increase with time.

    And now the question is how is your And now the question is how is your And now
    the question is how is your

    alpha chosen? If let''s say you you pick alpha chosen? If let''s say you you pick
    alpha chosen? If let''s say you you pick

    beta to begin with, you have a specific beta to begin with, you have a specific
    beta to begin with, you have a specific

    noise schedule in which you mention how noise schedule in which you mention how
    noise schedule in which you mention how

    beta uh how beta changes with every beta uh how beta changes with every beta uh
    how beta changes with every

    iteration. This is beta 1, this is beta iteration. This is beta 1, this is beta
    iteration. This is beta 1, this is beta

    2, this is beta 3. How do you 2, this is beta 3. How do you 2, this is beta 3.
    How do you

    uh find out values for your alphas? uh find out values for your alphas?'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 39
  start_sec: 2438.88
  end_sec: 2505.28
  text: 'uh find out values for your alphas?

    And this is something which uh even I And this is something which uh even I And
    this is something which uh even I

    was thinking for some time how are the was thinking for some time how are the
    was thinking for some time how are the

    values of alphas decided. values of alphas decided. values of alphas decided.

    So uh So uh

    what I realized is that let''s say if you what I realized is that let''s say if
    you what I realized is that let''s say if you

    have values of alphas as also increasing have values of alphas as also increasing
    have values of alphas as also increasing

    with with with

    every uh every transition right every uh every transition right every uh every
    transition right

    so then what you have is you have a so then what you have is you have a so then
    what you have is you have a

    final image final image final image

    with the mean also decreasing and the with the mean also decreasing and the with
    the mean also decreasing and the

    variation of that image or the standard variation of that image or the standard
    variation of that image or the standard

    deviation actually goes on increasing. deviation actually goes on increasing.
    deviation actually goes on increasing.

    >> [snorts] >> [snorts]

    >> So you want to ensure that this final >> So you want to ensure that this final
    >> So you want to ensure that this final

    image that you get image that you get image that you get

    it has a mean of zero it has a mean of zero it has a mean of zero

    and it has a variance of one ideally. So to achieve this variation of one you
    So to achieve this variation of one you

    need to have some normalization in these need to have some normalization in these
    need to have some normalization in these

    transition kernels. And the way it is transition kernels. And the way it is transition
    kernels. And the way it is

    done is you have you you choose alpha done is you have you you choose alpha done
    is you have you you choose alpha

    such that alpha square + beta square such that alpha square + beta square'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 40
  start_sec: 2505.28
  end_sec: 2601.119
  text: 'such that alpha square + beta square

    always becomes one. That is how you choose these alphas and That is how you choose
    these alphas and

    bet alphas. After you first choose the bet alphas. After you first choose the
    bet alphas. After you first choose the

    betas using the noise scheduleuler, you betas using the noise scheduleuler, you
    betas using the noise scheduleuler, you

    choose the alpha such that alpha square choose the alpha such that alpha square
    choose the alpha such that alpha square

    + beta square is equal to 1. + beta square is equal to 1. + beta square is equal
    to 1.

    So now you have these forward gshian So now you have these forward gshian So now
    you have these forward gshian

    transition kernels perfectly defined. transition kernels perfectly defined. transition
    kernels perfectly defined.

    And with this formulation in place, we And with this formulation in place, we
    And with this formulation in place, we

    can actually transform can actually transform can actually transform

    any image into pure noise. And it''s it''ll be interesting to see And it''s it''ll
    be interesting to see

    this for a practical example, right? how this for a practical example, right?
    how this for a practical example, right? how

    how this works out how this works out how this works out

    because theory is always very because theory is always very because theory is
    always very

    interesting but unless we apply it to interesting but unless we apply it to interesting
    but unless we apply it to

    practice practice practice

    we won''t get the confidence of uh we won''t get the confidence of uh we won''t
    get the confidence of uh

    using it in in in practical use cases. using it in in in practical use cases.
    using it in in in practical use cases.

    So let''s let''s look at an example where So let''s let''s look at an example
    where So let''s let''s look at an example where

    we apply this standard forward diffusion we apply this standard forward diffusion
    we apply this standard forward diffusion

    process to simple English letters. Okay. So uh the first step here is let Okay.
    So uh the first step here is let

    us connect it to a processor first. Okay. So in the first step we import our'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 41
  start_sec: 2601.119
  end_sec: 2661.68
  text: 'Okay. So in the first step we import our

    libraries. We are going to use numpy and libraries. We are going to use numpy
    and libraries. We are going to use numpy and

    uh mattplot lab for this example. So we uh mattplot lab for this example. So we
    uh mattplot lab for this example. So we

    import this and run these libraries. import this and run these libraries. import
    this and run these libraries.

    Then we create a simple Then we create a simple Then we create a simple

    letter image. So here we are drawing a letter image. So here we are drawing a
    letter image. So here we are drawing a

    simple image which is a letter t. Now the third block is something which Now the
    third block is something which

    is very important and this is where we is very important and this is where we
    is very important and this is where we

    should uh pay attention to should uh pay attention to should uh pay attention
    to

    how the alphas and betas are defined. So how the alphas and betas are defined.
    So how the alphas and betas are defined. So

    the first step is where you see the the first step is where you see the the first
    step is where you see the

    number of diffusion steps which is 100. number of diffusion steps which is 100.
    number of diffusion steps which is 100.

    So in this image I had only six steps So in this image I had only six steps So
    in this image I had only six steps

    over here or I think I had four steps. over here or I think I had four steps.
    over here or I think I had four steps.

    Yeah, add add four diffusers. Yeah, add add four diffusers. Yeah, add add four
    diffusers.

    But now we have 100 diffusion steps, But now we have 100 diffusion steps, But
    now we have 100 diffusion steps,

    which means that the the image is going which means that the the image is going
    which means that the the image is going

    to go from initial letter T to noise to go from initial letter T to noise to go
    from initial letter T to noise

    after 100 different steps. after 100 different steps.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 42
  start_sec: 2661.68
  end_sec: 2721.92
  text: 'after 100 different steps.

    Maybe this number you might not even Maybe this number you might not even Maybe
    this number you might not even

    require to be this high, but people require to be this high, but people require
    to be this high, but people

    usually keep it high to to begin with. usually keep it high to to begin with.
    usually keep it high to to begin with.

    Now you choose your standard deviation Now you choose your standard deviation
    Now you choose your standard deviation

    beta. So you can see that we have chosen beta. So you can see that we have chosen
    beta. So you can see that we have chosen

    it to go from 01 to 30 it to go from 01 to 30 it to go from 01 to 30

    uh in in sequence. So it is it is uh in in sequence. So it is it is uh in in sequence.
    So it is it is

    something like it''s let''s let''s try to something like it''s let''s let''s try
    to something like it''s let''s let''s try to

    see it''s it''s like a ramp basically it see it''s it''s like a ramp basically
    it see it''s it''s like a ramp basically it

    goes like this. This is where t equal goes like this. This is where t equal goes
    like this. This is where t equal

    to0 this is for t equal to0 and uh this is this is for t equal to0 and uh this
    is

    for t= 100. for t= 100. for t= 100.

    So your noise gradually increases for So your noise gradually increases for So
    your noise gradually increases for

    every single transition that you apply and alpha is chosen such that alpha and
    alpha is chosen such that alpha

    squar + beta square is 1. So alpha is squar + beta square is 1. So alpha is squar
    + beta square is 1. So alpha is

    chosen as roo<unk> of 1 - beta square. chosen as roo<unk> of 1 - beta square.
    chosen as roo<unk> of 1 - beta square.

    So this this makes sense now based on So this this makes sense now based on So
    this this makes sense now based on

    our discussion as well. So let me run our discussion as well. So let me run'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 43
  start_sec: 2721.92
  end_sec: 2775.27
  text: 'our discussion as well. So let me run

    this. this. this.

    Okay. Now we do the u Okay. Now we do the u Okay. Now we do the u

    step-by-step forward diffusion process. step-by-step forward diffusion process.
    step-by-step forward diffusion process.

    Now there is a very interesting uh Now there is a very interesting uh Now there
    is a very interesting uh

    trick which I want to tell all of you trick which I want to tell all of you trick
    which I want to tell all of you

    and that trick is and that trick is and that trick is

    uh let''s say we uh you know I I told you uh let''s say we uh you know I I told
    you uh let''s say we uh you know I I told you

    for every single pixel what we do is we for every single pixel what we do is we
    for every single pixel what we do is we

    like first we began by saying that we like first we began by saying that we like
    first we began by saying that we

    keep the mean same and just add noise keep the mean same and just add noise keep
    the mean same and just add noise

    right so uh is is there a simple way to right so uh is is there a simple way to
    right so uh is is there a simple way to

    write the new value for this pixel like write the new value for this pixel like
    write the new value for this pixel like

    let''s say the first value is 0.5 5 and let''s say the first value is 0.5 5 and
    let''s say the first value is 0.5 5 and

    then you create a a gshian distribution then you create a a gshian distribution
    then you create a a gshian distribution

    with a mean of 0.5 and a standard with a mean of 0.5 and a standard with a mean
    of 0.5 and a standard

    deviation of beta uh beta 1. So how do deviation of beta uh beta 1. So how do
    deviation of beta uh beta 1. So how do

    you find the new value of this? you find the new value of this? you find the new
    value of this?

    So it''s it''s it''s it''s a simple trick'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 44
  start_sec: 2775.27
  end_sec: 2846.79
  text: 'So it''s it''s it''s it''s a simple trick So it''s it''s it''s it''s a simple
    trick

    which is to say that you which is to say that you which is to say that you

    uh keep the original value or rather you can say you keep the mean or rather you
    can say you keep the mean

    whatever the mean is and then add it whatever the mean is and then add it whatever
    the mean is and then add it

    with the standard deviation with the standard deviation with the standard deviation

    and multiply it by a random number which and multiply it by a random number which
    and multiply it by a random number which

    goes between 0 and 1. goes between 0 and 1. goes between 0 and 1.

    [snorts] Okay. So now here let''s say the [snorts] Okay. So now here let''s say
    the [snorts] Okay. So now here let''s say the

    mean is we fix the mean to be 0.5 mean is we fix the mean to be 0.5 mean is we
    fix the mean to be 0.5

    and the standard deviation is how much and the standard deviation is how much
    and the standard deviation is how much

    here uh here uh here uh

    okay I have not given the value of beta okay I have not given the value of beta
    okay I have not given the value of beta

    1 but let''s say the standard deviation 1 but let''s say the standard deviation
    1 but let''s say the standard deviation

    is 0.1 so.5 plus.1 is 0.1 so.5 plus.1 is 0.1 so.5 plus.1

    into epsilon you can choose any value so into epsilon you can choose any value
    so into epsilon you can choose any value so

    let''s say for the first time I pick a let''s say for the first time I pick a
    let''s say for the first time I pick a

    value of 0.1 So this is how the mean changes. So this is how the mean changes.

    This is how the pixel value changes at This is how the pixel value changes at
    This is how the pixel value changes at

    every every every

    uh for every pixel. Now as we have seen uh for every pixel. Now as we have seen
    uh for every pixel. Now as we have seen

    before here the mu gets changed by'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 45
  start_sec: 2846.79
  end_sec: 2904.63
  text: 'before here the mu gets changed by before here the mu gets changed by

    alpha* alpha* alpha*

    alpha* the original pixel value and the alpha* the original pixel value and the
    alpha* the original pixel value and the

    beta is anyways beta 1 beta 2 beta 3 beta is anyways beta 1 beta 2 beta 3 beta
    is anyways beta 1 beta 2 beta 3

    etc. [snorts] So this is exactly what etc. [snorts] So this is exactly what etc.
    [snorts] So this is exactly what

    they have done here. they have done here. they have done here.

    You see this is the this is alpha * xt You see this is the this is alpha * xt
    You see this is the this is alpha * xt

    which is the new mean which is mu in which is the new mean which is mu in which
    is the new mean which is mu in

    this formula this formula this formula

    and then this is the beta which is and then this is the beta which is and then
    this is the beta which is

    standard deviation which is sigma in standard deviation which is sigma in standard
    deviation which is sigma in

    this formula and this is a zed is just a this formula and this is a zed is just
    a this formula and this is a zed is just a

    random variable which goes between 0 to random variable which goes between 0 to
    random variable which goes between 0 to

    one. So this is the randomized variable one. So this is the randomized variable
    one. So this is the randomized variable

    zed which which they have chosen zed which which they have chosen zed which which
    they have chosen

    and uh the dimensions of zed appear like and uh the dimensions of zed appear like
    and uh the dimensions of zed appear like

    this because the original image this because the original image this because the
    original image

    dimensions are h by w. So you have a dimensions are h by w. So you have a dimensions
    are h by w. So you have a

    height of 64x 64 right. So you have height of 64x 64 right. So you have height
    of 64x 64 right. So you have

    total of 64x 64 pixels and for every'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 46
  start_sec: 2904.63
  end_sec: 2951.44
  text: 'total of 64x 64 pixels and for every total of 64x 64 pixels and for every

    single pixel we choose a random variable single pixel we choose a random variable
    single pixel we choose a random variable

    uh which which goes from 0 to one. So, uh which which goes from 0 to one. So,
    uh which which goes from 0 to one. So,

    so that''s all this is the uh forward so that''s all this is the uh forward so
    that''s all this is the uh forward

    diffusion process. You go step by step. diffusion process. You go step by step.
    diffusion process. You go step by step.

    You might be thinking that why do we You might be thinking that why do we You
    might be thinking that why do we

    need to go step by step? Why can''t we need to go step by step? Why can''t we
    need to go step by step? Why can''t we

    just write one single mean and single just write one single mean and single just
    write one single mean and single

    variance and directly go to noise variance and directly go to noise variance and
    directly go to noise

    and that that in fact is a question and that that in fact is a question and that
    that in fact is a question

    which uh which uh which uh

    which which which makes sense. But I which which which makes sense. But I which
    which which makes sense. But I

    think the reason this is done is because think the reason this is done is because
    think the reason this is done is because

    remember encoder is not the final story remember encoder is not the final story
    remember encoder is not the final story

    here. We have the decoder also which is here. We have the decoder also which is
    here. We have the decoder also which is

    we want to learn how to go back from we want to learn how to go back from we want
    to learn how to go back from

    noise to the original image [snorts] and noise to the original image [snorts]
    and noise to the original image [snorts] and

    there it really helps if we go step by there it really helps if we go step by'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 47
  start_sec: 2951.44
  end_sec: 2996.88
  text: 'there it really helps if we go step by

    step right you can''t generate an image step right you can''t generate an image
    step right you can''t generate an image

    directly from noise that is too much directly from noise that is too much directly
    from noise that is too much

    pressure on the decoder. pressure on the decoder. pressure on the decoder.

    So to ease the pressure on the decoder So to ease the pressure on the decoder
    So to ease the pressure on the decoder

    and uh to make sure that you go step by and uh to make sure that you go step by
    and uh to make sure that you go step by

    step so that you first learn the first step so that you first learn the first
    step so that you first learn the first

    transition then the second and then you transition then the second and then you
    transition then the second and then you

    move towards noise. That is something move towards noise. That is something move
    towards noise. That is something

    which is more doable. Right? [snorts] It which is more doable. Right? [snorts]
    It which is more doable. Right? [snorts] It

    is something that humans also think in is something that humans also think in
    is something that humans also think in

    the same way. If we want to learn a the same way. If we want to learn a the same
    way. If we want to learn a

    concept we don''t directly jump to the concept we don''t directly jump to the
    concept we don''t directly jump to the

    final answer. We go step by step. And final answer. We go step by step. And final
    answer. We go step by step. And

    that''s why we have this uh stepbystep that''s why we have this uh stepbystep
    that''s why we have this uh stepbystep

    forward diffusion process. Okay, now we can actually visualize how Okay, now we
    can actually visualize how

    this becomes noise. You can run this and this becomes noise. You can run this
    and this becomes noise. You can run this and

    then you can see slowly and steadily the then you can see slowly and steadily
    the then you can see slowly and steadily the

    structure disappears and it becomes structure disappears and it becomes'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 48
  start_sec: 2996.88
  end_sec: 3055.19
  text: 'structure disappears and it becomes

    uniform. So it satisfies our original uniform. So it satisfies our original uniform.
    So it satisfies our original

    criteria that if we want this to be criteria that if we want this to be criteria
    that if we want this to be

    called as a diffusion process, the called as a diffusion process, the called as
    a diffusion process, the

    structure should slowly disappear with structure should slowly disappear with
    structure should slowly disappear with

    time. time. time.

    And I think the number of time steps as And I think the number of time steps as
    And I think the number of time steps as

    100 also make a lot of sense because 100 also make a lot of sense because 100
    also make a lot of sense because

    it''s not becoming noise at 60 or 80. So it''s not becoming noise at 60 or 80.
    So it''s not becoming noise at 60 or 80. So

    that''s why they have chosen a time step that''s why they have chosen a time step
    that''s why they have chosen a time step

    of 100. Okay. So uh Okay. So uh

    this is the forward diffusion process this is the forward diffusion process this
    is the forward diffusion process

    and u alphas and betas are the factors and u alphas and betas are the factors
    and u alphas and betas are the factors

    by which you scale the mean and beta is by which you scale the mean and beta is
    by which you scale the mean and beta is

    the standard deviation. the standard deviation. the standard deviation.

    Now there is a simple way to you know go Now there is a simple way to you know
    go Now there is a simple way to you know go

    from let''s say we want to find a formula from let''s say we want to find a formula
    from let''s say we want to find a formula

    which takes us from the original image which takes us from the original image
    which takes us from the original image

    to the third transition. Let''s say to the third transition. Let''s say to the
    third transition. Let''s say

    directly from this. So let''s say if I directly from this. So let''s say if I
    directly from this. So let''s say if I

    want to go directly from here to here.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 49
  start_sec: 3055.19
  end_sec: 3112.079
  text: 'want to go directly from here to here. want to go directly from here to here.

    So there is a way to uh write the mean So there is a way to uh write the mean
    So there is a way to uh write the mean

    and there is a way to write the and there is a way to write the and there is a
    way to write the

    deviation for that as well. Uh but we deviation for that as well. Uh but we deviation
    for that as well. Uh but we

    are going to look at it in the next are going to look at it in the next are going
    to look at it in the next

    section. section. section.

    But intuitively you can understand But intuitively you can understand But intuitively
    you can understand

    right? Since this is a gshian and this right? Since this is a gshian and this
    right? Since this is a gshian and this

    is a goshian we can write a goshian is a goshian we can write a goshian is a goshian
    we can write a goshian

    which directly goes from this to which directly goes from this to which directly
    goes from this to

    actually it goes from this to this point actually it goes from this to this point
    actually it goes from this to this point

    here. Okay. So a homework problem for all of Okay. So a homework problem for all
    of

    you is to you is to you is to

    write down the mean and the variance to write down the mean and the variance to
    write down the mean and the variance to

    take us from the original image in the take us from the original image in the
    take us from the original image in the

    data to any point in this transition data to any point in this transition data
    to any point in this transition

    cycle. For example, if I give you this cycle. For example, if I give you this
    cycle. For example, if I give you this

    point, write down the effective mean and point, write down the effective mean
    and point, write down the effective mean and

    the effective variance for this the effective variance for this the effective
    variance for this

    transition. If I give this as the transition. If I give this as the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 50
  start_sec: 3112.079
  end_sec: 3157.92
  text: 'transition. If I give this as the

    output, then write down the effective output, then write down the effective output,
    then write down the effective

    mean and the effective variance for this mean and the effective variance for this
    mean and the effective variance for this

    transition. transition. transition.

    So you can use this simple trick that we So you can use this simple trick that
    we So you can use this simple trick that we

    used for each transition and write it used for each transition and write it used
    for each transition and write it

    down multiple times. So you can see how down multiple times. So you can see how
    down multiple times. So you can see how

    the mean changes. First thing we can see the mean changes. First thing we can
    see the mean changes. First thing we can see

    is that the mean will I think get is that the mean will I think get is that the
    mean will I think get

    multiplied as mu1 into mu2 into mu3 etc. multiplied as mu1 into mu2 into mu3 etc.
    multiplied as mu1 into mu2 into mu3 etc.

    But this is a homework for all of you But this is a homework for all of you But
    this is a homework for all of you

    just sit down and write this down so just sit down and write this down so just
    sit down and write this down so

    that you will understand it. Remember that you will understand it. Remember that
    you will understand it. Remember

    what we started out in the beginning. We what we started out in the beginning.
    We what we started out in the beginning. We

    wanted to basically correlate the wanted to basically correlate the wanted to
    basically correlate the

    diffusion in physics to something with diffusion in physics to something with
    diffusion in physics to something with

    data and we realized that we can do that data and we realized that we can do that
    data and we realized that we can do that

    with two simple tenets of diffusion. The with two simple tenets of diffusion.
    The with two simple tenets of diffusion. The

    first tenet is the structure should first tenet is the structure should first
    tenet is the structure should

    disappear and the second tenant is the disappear and the second tenant is the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 51
  start_sec: 3157.92
  end_sec: 3211.839
  text: 'disappear and the second tenant is the

    structure should become uniform with structure should become uniform with structure
    should become uniform with

    time. This is exactly what we did with time. This is exactly what we did with
    time. This is exactly what we did with

    gshian kernels. gshian kernels. gshian kernels.

    So we have completed the forward So we have completed the forward So we have completed
    the forward

    diffusion process. Now the question diffusion process. Now the question diffusion
    process. Now the question

    remains what about the decoder? How does remains what about the decoder? How does
    remains what about the decoder? How does

    it look like? And how can we learn the it look like? And how can we learn the
    it look like? And how can we learn the

    original data distribution? original data distribution? original data distribution?

    If we draw parallels to how we If we draw parallels to how we If we draw parallels
    to how we

    constructed the variational constructed the variational constructed the variational

    autoenccoder, we can quickly see that autoenccoder, we can quickly see that autoenccoder,
    we can quickly see that

    the main difference is here we have a the main difference is here we have a the
    main difference is here we have a

    encoder which is fixed and now we are encoder which is fixed and now we are encoder
    which is fixed and now we are

    thinking about the decoder which is thinking about the decoder which is thinking
    about the decoder which is

    learnable. learnable. learnable.

    So the decoder has to be some kind of a So the decoder has to be some kind of
    a So the decoder has to be some kind of a

    neural network which we are learning. neural network which we are learning. neural
    network which we are learning.

    But then how do we construct the loss? But then how do we construct the loss?
    But then how do we construct the loss?

    How how do we predict the original image How how do we predict the original image
    How how do we predict the original image

    just from noise? That is the problem just from noise? That is the problem just
    from noise? That is the problem

    that we are going to handle right now. that we are going to handle right now.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 52
  start_sec: 3211.839
  end_sec: 3266.0
  text: 'that we are going to handle right now.

    So the the first intuition probably So the the first intuition probably So the
    the first intuition probably

    tells us that to go from noise to the tells us that to go from noise to the tells
    us that to go from noise to the

    original data, you might have to remove original data, you might have to remove
    original data, you might have to remove

    noise in a very specific way from the noise in a very specific way from the noise
    in a very specific way from the

    image because the way you remove noise image because the way you remove noise
    image because the way you remove noise

    is going to influence what your forward is going to influence what your forward
    is going to influence what your forward

    or or your final image looks like. For or or your final image looks like. For
    or or your final image looks like. For

    example, if I want to go from noise to a example, if I want to go from noise to
    a example, if I want to go from noise to a

    cat, cat, cat,

    then I need to remove noise in a very then I need to remove noise in a very then
    I need to remove noise in a very

    specific way. I can''t remove it specific way. I can''t remove it specific way.
    I can''t remove it

    randomly. randomly. randomly.

    Now another question which might come to Now another question which might come
    to Now another question which might come to

    your mind is well we know the forward your mind is well we know the forward your
    mind is well we know the forward

    caution kernel right? caution kernel right? caution kernel right?

    So what if we do the same thing in the So what if we do the same thing in the
    So what if we do the same thing in the

    reverse way? For example, reverse way? For example, reverse way? For example,

    uh if we know that going from diffuser uh if we know that going from diffuser
    uh if we know that going from diffuser

    [clears throat] 4 to noise or going from [clears throat] 4 to noise or going from
    [clears throat] 4 to noise or going from

    this image to noise this image to noise'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 53
  start_sec: 3266.0
  end_sec: 3329.76
  text: 'this image to noise

    is is is

    maybe scaling the mean by alpha and maybe scaling the mean by alpha and maybe
    scaling the mean by alpha and

    adding beta. Why don''t we just upscale adding beta. Why don''t we just upscale
    adding beta. Why don''t we just upscale

    by alpha and remove the beta noise from by alpha and remove the beta noise from
    by alpha and remove the beta noise from

    each of these pixels? each of these pixels? each of these pixels?

    So So So

    why can''t we do the same thing that we why can''t we do the same thing that we
    why can''t we do the same thing that we

    did in the forward process did in the forward process did in the forward process

    in the reverse process? in the reverse process? in the reverse process?

    The main problem there is that The main problem there is that The main problem
    there is that

    when you''re dealing with actual data when you''re dealing with actual data when
    you''re dealing with actual data

    uh uh

    you have to reproduce the image directly you have to reproduce the image directly
    you have to reproduce the image directly

    from noise. from noise. from noise.

    So you won''t have access to the forward So you won''t have access to the forward
    So you won''t have access to the forward

    process as such. You won''t have access process as such. You won''t have access
    process as such. You won''t have access

    to the different means and variances you to the different means and variances
    you to the different means and variances you

    have used for every single diffuser. have used for every single diffuser. have
    used for every single diffuser.

    So that is something which will not be So that is something which will not be
    So that is something which will not be

    given to you. you just have noise and given to you. you just have noise and given
    to you. you just have noise and

    you have to recreate one original image you have to recreate one original image
    you have to recreate one original image

    from a sample or to create a sample from from a sample or to create a sample from
    from a sample or to create a sample from

    the original data. the original data.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 54
  start_sec: 3329.76
  end_sec: 3386.16
  text: 'the original data.

    So this will become clear as as we go So this will become clear as as we go So
    this will become clear as as we go

    along. Let''s let''s move along. along. Let''s let''s move along. along. Let''s
    let''s move along.

    So at its core the essence of DDPM lies So at its core the essence of DDPM lies
    So at its core the essence of DDPM lies

    in the ability to reverse the controlled in the ability to reverse the controlled
    in the ability to reverse the controlled

    degradation which is impo imposed by the degradation which is impo imposed by
    the degradation which is impo imposed by the

    forward diffusion process. forward diffusion process. forward diffusion process.

    Starting from pure unstructured noise, Starting from pure unstructured noise,
    Starting from pure unstructured noise,

    the objective is to progressively dn the objective is to progressively dn the
    objective is to progressively dn

    noiseise this randomness step by step noiseise this randomness step by step noiseise
    this randomness step by step

    until a coherent and a meaningful data until a coherent and a meaningful data
    until a coherent and a meaningful data

    sample emerges. sample emerges. sample emerges.

    So we have gone from data to noise and So we have gone from data to noise and
    So we have gone from data to noise and

    now we have to go back from noise to now we have to go back from noise to now
    we have to go back from noise to

    data. data. data.

    [snorts] For example, if we have let''s [snorts] For example, if we have let''s
    [snorts] For example, if we have let''s

    say a distribution two data distribution say a distribution two data distribution
    say a distribution two data distribution

    that is of cats, then this this this that is of cats, then this this this that
    is of cats, then this this this

    process this process should do something process this process should do something
    process this process should do something

    as follows. It should take noise and it as follows. It should take noise and it
    as follows. It should take noise and it

    should den noiseise it progressively and should den noiseise it progressively
    and should den noiseise it progressively and

    finally I should get cat finally I should get cat finally I should get cat

    right. So right. So'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 55
  start_sec: 3386.16
  end_sec: 3451.109
  text: 'right. So

    you can see that this is not like a you can see that this is not like a you can
    see that this is not like a

    one-time denoising step like we did for one-time denoising step like we did for
    one-time denoising step like we did for

    variation autoenccoder. There are a variation autoenccoder. There are a variation
    autoenccoder. There are a

    series of uh decoders here with series of uh decoders here with series of uh decoders
    here with

    different distributions. So we need to different distributions. So we need to
    different distributions. So we need to

    predict all those distributions predict all those distributions predict all those
    distributions

    properly. properly. properly.

    Okay. So the decoder distribution is Okay. So the decoder distribution is Okay.
    So the decoder distribution is

    denoted as P theta of X. denoted as P theta of X. denoted as P theta of X.

    And whatever we do in the reverse And whatever we do in the reverse And whatever
    we do in the reverse

    process, one thing we know that the process, one thing we know that the process,
    one thing we know that the

    final goal is to maximize the final goal is to maximize the final goal is to maximize
    the

    probability of sampling the images from probability of sampling the images from
    probability of sampling the images from

    the two data distribution. Which means the two data distribution. Which means
    the two data distribution. Which means

    that if the decoder distribution is that if the decoder distribution is that if
    the decoder distribution is

    denoted by P theta of X, denoted by P theta of X, denoted by P theta of X,

    if we substitute X0 instead of X, it if we substitute X0 instead of X, it if we
    substitute X0 instead of X, it

    means that what is the probability means that what is the probability means that
    what is the probability

    that that that

    uh the images which are drawn from the uh the images which are drawn from the
    uh the images which are drawn from the

    real data, what is the probability given real data, what is the probability given
    real data, what is the probability given

    to those images by your decoder? to those images by your decoder? to those images
    by your decoder?

    And that probability should be very'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 56
  start_sec: 3451.109
  end_sec: 3510.15
  text: 'And that probability should be very And that probability should be very

    high, right? because we want our decoder high, right? because we want our decoder
    high, right? because we want our decoder

    to assign higher probabilities to images to assign higher probabilities to images
    to assign higher probabilities to images

    which are sampled from the real data. which are sampled from the real data. which
    are sampled from the real data.

    So we want to maximize this and this is So we want to maximize this and this is
    So we want to maximize this and this is

    exactly the same objective that we exactly the same objective that we exactly
    the same objective that we

    started out with variational started out with variational started out with variational

    autoenccoders as well and this is what autoenccoders as well and this is what
    autoenccoders as well and this is what

    got decomposed into elbow where we had got decomposed into elbow where we had
    got decomposed into elbow where we had

    the reconstruction term and the the reconstruction term and the the reconstruction
    term and the

    regularization term. regularization term. regularization term.

    So we want to maximize the log of this. So we want to maximize the log of this.
    So we want to maximize the log of this.

    We want to maximize the likelihood of We want to maximize the likelihood of We
    want to maximize the likelihood of

    the images which are sampled from the the images which are sampled from the the
    images which are sampled from the

    real data. real data. real data.

    And just like we did for variation And just like we did for variation And just
    like we did for variation

    autoenccoders, there is a way to autoenccoders, there is a way to autoenccoders,
    there is a way to

    calculate the lower bound for calculate the lower bound for calculate the lower
    bound for

    uh uh this this evidence for this uh uh this this evidence for this uh uh this
    this evidence for this

    likelihood. There is a way to calculate likelihood. There is a way to calculate
    likelihood. There is a way to calculate

    a bound which is always lower than this. a bound which is always lower than this.
    a bound which is always lower than this.

    So if we maximize that lower bound it'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 57
  start_sec: 3510.15
  end_sec: 3574.4
  text: 'So if we maximize that lower bound it So if we maximize that lower bound
    it

    also means that we are maximized the also means that we are maximized the also
    means that we are maximized the

    true objective function. true objective function. true objective function.

    [cough] So the lower bound is denoted by this So the lower bound is denoted by
    this

    letter E and we can prove that E is letter E and we can prove that E is letter
    E and we can prove that E is

    composed of three terms. [snorts] composed of three terms. [snorts] composed of
    three terms. [snorts]

    The first term is the reconstruction The first term is the reconstruction The
    first term is the reconstruction

    term which tells you the probability of term which tells you the probability of
    term which tells you the probability of

    reconstructing the original image from reconstructing the original image from
    reconstructing the original image from

    the first transition. the first transition. the first transition.

    So basically probability of So basically probability of So basically probability
    of

    reconstructing the original image from reconstructing the original image from

    X1. X1. X1.

    The second term is the regularization The second term is the regularization The
    second term is the regularization

    term. Which means that term. Which means that term. Which means that

    we want our we want our we want our

    encoded data. Whatever our forward encoded data. Whatever our forward encoded
    data. Whatever our forward

    diffusion does, we want that as close as diffusion does, we want that as close
    as diffusion does, we want that as close as

    possible to pure noise. Now this is possible to pure noise. Now this is possible
    to pure noise. Now this is

    something which is fixed. We are already something which is fixed. We are already
    something which is fixed. We are already

    doing this. We know that if we apply the doing this. We know that if we apply
    the doing this. We know that if we apply the

    encoder, if we apply the gshian encoder, if we apply the gshian encoder, if we
    apply the gshian

    transition kernel that we looked at transition kernel that we looked at transition
    kernel that we looked at

    before, we are going to get pure noise before, we are going to get pure noise'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 58
  start_sec: 3574.4
  end_sec: 3626.71
  text: 'before, we are going to get pure noise

    only. So there is no doubt that this is only. So there is no doubt that this is
    only. So there is no doubt that this is

    going to be pure noise. So this is going to be pure noise. So this is going to
    be pure noise. So this is

    something that something that something that

    uh we will not consider because this is uh we will not consider because this is
    uh we will not consider because this is

    anyways going to be zero or maybe very anyways going to be zero or maybe very
    anyways going to be zero or maybe very

    close to zero. So the regularization close to zero. So the regularization close
    to zero. So the regularization

    term really does not play a big role in term really does not play a big role in
    term really does not play a big role in

    in this process. in this process. in this process.

    The third term is very very interesting The third term is very very interesting
    The third term is very very interesting

    and we will get to the heart of it but and we will get to the heart of it but
    and we will get to the heart of it but

    please understand the meaning of these please understand the meaning of these
    please understand the meaning of these

    symbols which are there in this third symbols which are there in this third symbols
    which are there in this third

    term. So the first is the KL divergence term. So the first is the KL divergence
    term. So the first is the KL divergence

    which is the difference between two which is the difference between two which
    is the difference between two

    probability distributions. probability distributions. probability distributions.

    So the if the probability distributions So the if the probability distributions
    So the if the probability distributions

    are close the KL divergence is very low are close the KL divergence is very low
    are close the KL divergence is very low

    but if the probability distributions are but if the probability distributions
    are but if the probability distributions are

    far then the KL divergence is high. far then the KL divergence is high. far then
    the KL divergence is high.

    So this is saying that I want to'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 59
  start_sec: 3626.71
  end_sec: 3692.72
  text: 'So this is saying that I want to So this is saying that I want to

    minimize the kale divergence between minimize the kale divergence between

    these two probabilities. these two probabilities. these two probabilities.

    Now what do these uh two probabilities Now what do these uh two probabilities
    Now what do these uh two probabilities

    mean? mean? mean?

    This is something which is called as the This is something which is called as
    the This is something which is called as the

    true posterior. It means that true posterior. It means that true posterior. It
    means that

    what is the what is the what is the

    probability of probability of probability of

    uh uh

    [snorts] [snorts]

    the previous image the previous image the previous image

    given the current image? What is the so given the current image? What is the so
    given the current image? What is the so

    how how can we go from the current image how how can we go from the current image
    how how can we go from the current image

    to the previous image to the previous image to the previous image

    if we also know the true data? If we if we also know the true data? If we if we
    also know the true data? If we

    also know the original image, also know the original image, also know the original
    image,

    what does that mean? Let''s say uh what what does that mean? Let''s say uh what
    what does that mean? Let''s say uh what

    I''m trying to say is what is the I''m trying to say is what is the I''m trying
    to say is what is the

    probability of going from or how do we probability of going from or how do we
    probability of going from or how do we

    go from x2 to x1 go from x2 to x1 go from x2 to x1

    if we know that finally we want to reach if we know that finally we want to reach
    if we know that finally we want to reach

    here here here

    that is what this says and the first is that is what this says and the first is
    that is what this says and the first is

    what we are trying to predict how do we what we are trying to predict how do we'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 60
  start_sec: 3692.72
  end_sec: 3744.16
  text: 'what we are trying to predict how do we

    actually go from x2 to x1 this is what actually go from x2 to x1 this is what
    actually go from x2 to x1 this is what

    our neural network will predict and our our neural network will predict and our
    our neural network will predict and our

    prediction should match match as close prediction should match match as close
    prediction should match match as close

    as possible to this. as possible to this. as possible to this.

    Please play pay a very close attention Please play pay a very close attention
    Please play pay a very close attention

    to this conditioning. We are to this conditioning. We are to this conditioning.
    We are

    conditioning on the true data and I will conditioning on the true data and I will
    conditioning on the true data and I will

    explain to you why this is very very explain to you why this is very very explain
    to you why this is very very

    important. important. important.

    [snorts] [snorts]

    Okay. So people what they do is they Okay. So people what they do is they Okay.
    So people what they do is they

    completely they don''t consider this term completely they don''t consider this
    term completely they don''t consider this term

    at all which is the reconstruction term. at all which is the reconstruction term.
    at all which is the reconstruction term.

    And I think the rational behind this is And I think the rational behind this is
    And I think the rational behind this is

    that people figure out that if we manage that people figure out that if we manage
    that people figure out that if we manage

    to to to

    uh match this reverse transition with uh match this reverse transition with uh
    match this reverse transition with

    the true transition or the true the true transition or the true the true transition
    or the true

    posterior, it means that our model is posterior, it means that our model is posterior,
    it means that our model is

    learning how to go from noise to the learning how to go from noise to the learning
    how to go from noise to the

    true data. So if we achieve this, then true data. So if we achieve this, then'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 61
  start_sec: 3744.16
  end_sec: 3791.109
  text: 'true data. So if we achieve this, then

    we are anyways going to achieve a we are anyways going to achieve a we are anyways
    going to achieve a

    reconstruction which is that is good. reconstruction which is that is good. reconstruction
    which is that is good.

    Having said that there are some Having said that there are some Having said that
    there are some

    formulations which also consider formulations which also consider formulations
    which also consider

    reconstruction but for the purpose of reconstruction but for the purpose of reconstruction
    but for the purpose of

    this paper we are going to ignore that this paper we are going to ignore that
    this paper we are going to ignore that

    which is what was done in the DDPM which is what was done in the DDPM which is
    what was done in the DDPM

    paper. So we are going to stick with paper. So we are going to stick with paper.
    So we are going to stick with

    that. that. that.

    Okay. So u these two terms are very Okay. So u these two terms are very Okay.
    So u these two terms are very

    similar to what we saw in VA. This is similar to what we saw in VA. This is similar
    to what we saw in VA. This is

    the third term which is the different the third term which is the different the
    third term which is the different

    term. Now to understand what we are term. Now to understand what we are term.
    Now to understand what we are

    essentially doing in this term because essentially doing in this term because
    essentially doing in this term because

    this is the only term that we want to this is the only term that we want to this
    is the only term that we want to

    focus on. We want to minimize the KL focus on. We want to minimize the KL focus
    on. We want to minimize the KL

    divergence between the transition the divergence between the transition the divergence
    between the transition the

    reverse transition kernel which is reverse transition kernel which is reverse
    transition kernel which is

    learned by our neural network and the learned by our neural network and the learned
    by our neural network and the

    true posterior. true posterior. true posterior.

    So let''s let''s take an example and if'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 62
  start_sec: 3791.109
  end_sec: 3848.47
  text: 'So let''s let''s take an example and if So let''s let''s take an example
    and if

    you are bothered by the word posterior you are bothered by the word posterior
    you are bothered by the word posterior

    don''t worry about it too much. It is don''t worry about it too much. It is don''t
    worry about it too much. It is

    basically something where basically something where basically something where

    uh it it it means that uh it it it means that uh it it it means that

    what is the true what is the true what is the true

    reverse transition kernel given the reverse transition kernel given the reverse
    transition kernel given the

    original data. Okay. So let''s let''s take an example to Okay. So let''s let''s
    take an example to

    understand this also. Okay. So uh understand this also. Okay. So uh understand
    this also. Okay. So uh

    imagine that this is XT, right? This is imagine that this is XT, right? This is
    imagine that this is XT, right? This is

    the image that we have at our current the image that we have at our current the
    image that we have at our current

    time step. And you can see that it''s time step. And you can see that it''s time
    step. And you can see that it''s

    it''s a blurred image because of the it''s a blurred image because of the it''s
    a blurred image because of the

    rain. So this is very similar to how our rain. So this is very similar to how
    our rain. So this is very similar to how our

    noisy image is going to look like. noisy image is going to look like. noisy image
    is going to look like.

    Now our objective is to find xt minus Now our objective is to find xt minus Now
    our objective is to find xt minus

    one. one. one.

    So you look at this and you say that how So you look at this and you say that
    how So you look at this and you say that how

    do I know what''s the previous image? So do I know what''s the previous image?
    So do I know what''s the previous image? So

    basically you''re saying that before the basically you''re saying that before
    the basically you''re saying that before the

    rain fell on this paper'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 63
  start_sec: 3848.47
  end_sec: 3900.4
  text: 'rain fell on this paper rain fell on this paper

    how did it look like? how did it look like? how did it look like?

    And that''s very hard to tell because And that''s very hard to tell because And
    that''s very hard to tell because

    it''s completely smudged. Right? I I have it''s completely smudged. Right? I I
    have it''s completely smudged. Right? I I have

    no idea how it looked like because it it no idea how it looked like because it
    it no idea how it looked like because it it

    it looks so smudged. it looks so smudged. it looks so smudged.

    So this is this is this is very So this is this is this is very So this is this
    is this is very

    difficult. Right? Now consider another difficult. Right? Now consider another
    difficult. Right? Now consider another

    case. What if you are asked the same case. What if you are asked the same case.
    What if you are asked the same

    question to predict xt minus one but you question to predict xt minus one but
    you question to predict xt minus one but you

    are given the original image x0. are given the original image x0. are given the
    original image x0.

    So, so you want to predict the image So, so you want to predict the image So,
    so you want to predict the image

    which comes just before this. But you which comes just before this. But you which
    comes just before this. But you

    are given the true image also. This is are given the true image also. This is
    are given the true image also. This is

    the image before the rail fell on this the image before the rail fell on this
    the image before the rail fell on this

    and it became this. and it became this. and it became this.

    So now we can clearly see that oh okay So now we can clearly see that oh okay
    So now we can clearly see that oh okay

    this this is supposed to be meat m. So this this is supposed to be meat m. So
    this this is supposed to be meat m. So

    maybe if I just remove some noise it maybe if I just remove some noise it'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 64
  start_sec: 3900.4
  end_sec: 3960.96
  text: 'maybe if I just remove some noise it

    will look something similar to meat. will look something similar to meat. will
    look something similar to meat.

    This will look something similar to me This will look something similar to me
    This will look something similar to me

    etc. etc. etc.

    Now it suddenly becomes much more easier Now it suddenly becomes much more easier
    Now it suddenly becomes much more easier

    to find xt minus one because we have to find xt minus one because we have to find
    xt minus one because we have

    access to the original image. access to the original image. access to the original
    image.

    [snorts] [snorts]

    So uh and and this is exactly what this So uh and and this is exactly what this
    So uh and and this is exactly what this

    true posterior means. true posterior means. true posterior means.

    Okay. So what we are trying to say here Okay. So what we are trying to say here
    Okay. So what we are trying to say here

    is try to predict the image which came is try to predict the image which came
    is try to predict the image which came

    just before the current image given the just before the current image given the
    just before the current image given the

    true image also. true image also. true image also.

    And it turns out that this is this is And it turns out that this is this is And
    it turns out that this is this is

    something we can calculate. something we can calculate. something we can calculate.

    How we can calculate this? Let''s take How we can calculate this? Let''s take
    How we can calculate this? Let''s take

    again go to Batman. Batman has been again go to Batman. Batman has been again
    go to Batman. Batman has been

    very supportive to us today. So in the very supportive to us today. So in the
    very supportive to us today. So in the

    forward diffusion process, we went from forward diffusion process, we went from
    forward diffusion process, we went from

    X0 to X4 X0 to X4 X0 to X4

    to pure noise. The question is how do to pure noise. The question is how do to
    pure noise. The question is how do

    you go from X3 to X2? you go from X3 to X2?'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 65
  start_sec: 3960.96
  end_sec: 4025.52
  text: 'you go from X3 to X2?

    That is the question. Okay, That is the question. Okay, That is the question.
    Okay,

    now now now

    you have access to x3 and you also have you have access to x3 and you also have
    you have access to x3 and you also have

    access to x0. access to x0. access to x0.

    So I know that in three time steps I So I know that in three time steps I So I
    know that in three time steps I

    need to remove this much noise. So in need to remove this much noise. So in need
    to remove this much noise. So in

    one time step I''ll just remove one/ird one time step I''ll just remove one/ird
    one time step I''ll just remove one/ird

    of that amount. So I can predict this. So this is something which is called as
    So this is something which is called as

    the true posterior and we want our the true posterior and we want our the true
    posterior and we want our

    neural network to match this as close as neural network to match this as close
    as neural network to match this as close as

    possible. possible. possible.

    Once you understand this, you understand Once you understand this, you understand
    Once you understand this, you understand

    that that

    training our neural network is going to training our neural network is going to
    training our neural network is going to

    depend on how well we estimate this true depend on how well we estimate this true
    depend on how well we estimate this true

    posterior. If we are able to estimate posterior. If we are able to estimate posterior.
    If we are able to estimate

    this properly, this properly, this properly,

    we can try to find out a reverse process we can try to find out a reverse process
    we can try to find out a reverse process

    which which matches this as close as which which matches this as close as which
    which matches this as close as

    possible. possible.

    Now you might say that uh Raj this is Now you might say that uh Raj this is Now
    you might say that uh Raj this is

    fine but if we are able to predict this fine but if we are able to predict this'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 66
  start_sec: 4025.52
  end_sec: 4098.229
  text: 'fine but if we are able to predict this

    why can''t we just why can''t we just why can''t we just

    match this directly to this? If if we match this directly to this? If if we match
    this directly to this? If if we

    can predict this can predict this can predict this

    the reason we can''t do that is because the reason we can''t do that is because
    the reason we can''t do that is because

    x0 is not given to us in test time in x0 is not given to us in test time in x0
    is not given to us in test time in

    test time we are only given noise. test time we are only given noise. test time
    we are only given noise.

    So the idea is to predict this So the idea is to predict this So the idea is to
    predict this

    distribution distribution distribution

    for all the images in the true data and for all the images in the true data and
    for all the images in the true data and

    then find a neural network which then find a neural network which then find a
    neural network which

    understands understands understands

    how the data is going back from noise to how the data is going back from noise
    to how the data is going back from noise to

    the original data and find a function the original data and find a function the
    original data and find a function

    which kind of averages all those which kind of averages all those which kind of
    averages all those

    trajectories. trajectories. trajectories.

    So, so what I mean is let''s say this is So, so what I mean is let''s say this
    is So, so what I mean is let''s say this is

    the original image which is X0 and this is noise okay this is like and this is
    noise okay this is like

    complete noise uh forgive my handwriting I don''t have uh forgive my handwriting
    I don''t have

    access to the board today and let''s say access to the board today and let''s
    say access to the board today and let''s say

    okay this is okay this is okay this is

    this is the original data distribution this is the original data distribution
    this is the original data distribution

    by the way this is one path that you'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 67
  start_sec: 4098.229
  end_sec: 4154.719
  text: 'by the way this is one path that you by the way this is one path that you

    take from the noise to the data data. take from the noise to the data data. take
    from the noise to the data data.

    This is another path that you take to This is another path that you take to This
    is another path that you take to

    the from the noise to the data. This is the from the noise to the data. This is
    the from the noise to the data. This is

    so there are there are many paths which so there are there are many paths which
    so there are there are many paths which

    you can take and you exactly know these you can take and you exactly know these
    you can take and you exactly know these

    paths which is the true posterior. Now paths which is the true posterior. Now
    paths which is the true posterior. Now

    what we are trying to do is we are what we are trying to do is we are what we
    are trying to do is we are

    trying to look at all these paths and we trying to look at all these paths and
    we trying to look at all these paths and we

    are trying to learn from these parts. We are trying to learn from these parts.
    We are trying to learn from these parts. We

    are trying to understand okay I know all are trying to understand okay I know
    all are trying to understand okay I know all

    these parts. What is something that is these parts. What is something that is
    these parts. What is something that is

    common in all these parts? How can I common in all these parts? How can I common
    in all these parts? How can I

    learn to learn the reverse process learn to learn the reverse process learn to
    learn the reverse process

    properly? This is what our neural properly? This is what our neural properly?
    This is what our neural

    network tries to learn. And this is the intuition behind this And this is the
    intuition behind this

    term. Okay. So let''s let''s try to uh Okay. So let''s let''s try to uh

    understand first how how this posterior understand first how how this posterior'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 68
  start_sec: 4154.719
  end_sec: 4229.83
  text: 'understand first how how this posterior

    is is predicted. is is predicted. is is predicted.

    It turns out that this this reverse It turns out that this this reverse It turns
    out that this this reverse

    process process process

    it can be approximated by a gshian it can be approximated by a gshian it can be
    approximated by a gshian

    distribution which has a mean and a distribution which has a mean and a distribution
    which has a mean and a

    variance. So okay how how how is that written? So So okay how how how is that
    written? So

    the mean is written as the mean is written as the mean is written as

    mu of x i comma x0. So the mean is dependent on the current So the mean is dependent
    on the current

    image which is this image image which is this image image which is this image

    and it''s dependent on the original image and it''s dependent on the original
    image and it''s dependent on the original image

    which which makes sense and the variance which which makes sense and the variance
    which which makes sense and the variance

    is only dependent on the current time is only dependent on the current time is
    only dependent on the current time

    step. step. step.

    [snorts] [snorts]

    So intuitively we expect the mean to So intuitively we expect the mean to So intuitively
    we expect the mean to

    depend on the original image as well as depend on the original image as well as
    depend on the original image as well as

    the image at the current time step. So the image at the current time step. So
    the image at the current time step. So

    it is given by this function which is a1 it is given by this function which is
    a1 it is given by this function which is a1

    * x0 * x0 * x0

    plus a2 * x i. plus a2 * x i. plus a2 * x i.

    So what does this mean? Let''s say I want So what does this mean? Let''s say I
    want So what does this mean? Let''s say I want

    to go back from to go back from to go back from

    x3 to x2. x3 to x2. x3 to x2.

    How much importance should I place on X3'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 69
  start_sec: 4229.83
  end_sec: 4286.56
  text: 'How much importance should I place on X3 How much importance should I place
    on X3

    and how much importance should I place and how much importance should I place
    and how much importance should I place

    on X0? on X0? on X0?

    Intuitively, you might expect that as we Intuitively, you might expect that as
    we Intuitively, you might expect that as we

    move closer to the true image, the move closer to the true image, the move closer
    to the true image, the

    emphasize on X0 will increase and the emphasize on X0 will increase and the emphasize
    on X0 will increase and the

    emphasize on the previous image will emphasize on the previous image will emphasize
    on the previous image will

    reduce. reduce. reduce.

    So, A1 and A2 are are functions of the So, A1 and A2 are are functions of the
    So, A1 and A2 are are functions of the

    noise schedule. Uh noise schedule. Uh noise schedule. Uh

    however the intuition is that however the intuition is that however the intuition
    is that

    the importance given to the original the importance given to the original the
    importance given to the original

    image will increase as we move closer image will increase as we move closer image
    will increase as we move closer

    and closer in the reverse transition and closer in the reverse transition and
    closer in the reverse transition

    process to the original image and the process to the original image and the process
    to the original image and the

    importance of this will decrease as we importance of this will decrease as we
    importance of this will decrease as we

    move closer and closer to the original move closer and closer to the original
    move closer and closer to the original

    image. image.

    So intuitively I expect these graphs to So intuitively I expect these graphs to
    So intuitively I expect these graphs to

    move like this. A1 should basically move like this. A1 should basically move like
    this. A1 should basically

    increase and A2 should decrease increase and A2 should decrease increase and A2
    should decrease

    with time in the reverse transition with time in the reverse transition with time
    in the reverse transition

    process. And I think we do have a graph process. And I think we do have a graph'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 70
  start_sec: 4286.56
  end_sec: 4348.96
  text: 'process. And I think we do have a graph

    which talks about it. Yeah. Yeah. Here. which talks about it. Yeah. Yeah. Here.
    which talks about it. Yeah. Yeah. Here.

    So here you see that uh the weightage on So here you see that uh the weightage
    on So here you see that uh the weightage on

    the original image X the original image X the original image X

    it actually if you look at uh time step it actually if you look at uh time step
    it actually if you look at uh time step

    let''s see okay so the blue curve reduces with time okay so the blue curve reduces
    with time

    and the orange curve increases with time and the orange curve increases with time
    and the orange curve increases with time

    but I think the notation of time is but I think the notation of time is but I
    think the notation of time is

    reversed here. So if you look at the reversed here. So if you look at the reversed
    here. So if you look at the

    weight on the original image in [snorts] weight on the original image in [snorts]
    weight on the original image in [snorts]

    this graph, it appears that the weight this graph, it appears that the weight
    this graph, it appears that the weight

    on the original image is reducing on the original image is reducing on the original
    image is reducing

    U. U. U.

    But according to my intuition, it should But according to my intuition, it should
    But according to my intuition, it should

    be reversed. And the reason why that is be reversed. And the reason why that is
    be reversed. And the reason why that is

    is because here time t= t is most noisy is because here time t= t is most noisy
    is because here time t= t is most noisy

    and time t= 1 is the least noisy. So and time t= 1 is the least noisy. So and
    time t= 1 is the least noisy. So

    basically we are going from this to this basically we are going from this to this
    basically we are going from this to this

    here. here. here.

    So, so you should read the time as this So, so you should read the time as this'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 71
  start_sec: 4348.96
  end_sec: 4403.03
  text: 'So, so you should read the time as this

    this to this. So, here we have the this to this. So, here we have the this to
    this. So, here we have the

    complete noisy image complete noisy image complete noisy image

    and here we have the true image. So, so, and here we have the true image. So,
    so, and here we have the true image. So, so,

    so it makes sense that as we move from so it makes sense that as we move from
    so it makes sense that as we move from

    noisy image to the true image, as we go noisy image to the true image, as we go
    noisy image to the true image, as we go

    closer to the true image, the weight on closer to the true image, the weight on
    closer to the true image, the weight on

    the original image increases and as we move closer to the true image, the as we
    move closer to the true image, the

    weight on the noisy image decreases. So weight on the noisy image decreases. So
    weight on the noisy image decreases. So

    you can see the blue curve increases as you can see the blue curve increases as
    you can see the blue curve increases as

    we go towards zero and the orange curve we go towards zero and the orange curve
    we go towards zero and the orange curve

    decreases as we go towards zero which is decreases as we go towards zero which
    is decreases as we go towards zero which is

    exactly what our intuition says. exactly what our intuition says. exactly what
    our intuition says.

    So this is something which is one of the So this is something which is one of
    the So this is something which is one of the

    key findings of this paper is that the key findings of this paper is that the
    key findings of this paper is that the

    reverse transition true posterior reverse transition true posterior reverse transition
    true posterior

    can be written as a gshian with this can be written as a gshian with this can
    be written as a gshian with this

    mean and the sigma also can be written mean and the sigma also can be written
    mean and the sigma also can be written

    as a3 which is a function of all these'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 72
  start_sec: 4403.03
  end_sec: 4487.36
  text: 'as a3 which is a function of all these as a3 which is a function of all these

    variances. variances. variances.

    So basically you go from uh the original So basically you go from uh the original
    So basically you go from uh the original

    image to the noisy image. [snorts] image to the noisy image. [snorts] image to
    the noisy image. [snorts]

    Okay. Now the main question is here okay Okay. Now the main question is here okay
    Okay. Now the main question is here okay

    fine this is all right but can we fine this is all right but can we fine this
    is all right but can we

    actually implement this and see if we actually implement this and see if we actually
    implement this and see if we

    can use this formula to go from noise to can use this formula to go from noise
    to can use this formula to go from noise to

    the true image. So let''s let''s try to the true image. So let''s let''s try to
    the true image. So let''s let''s try to

    see if we can do that. [snorts]

    >> Okay. So, first we uh connect it to a >> Okay. So, first we uh connect it to
    a >> Okay. So, first we uh connect it to a

    GPU and then we uh import a single image and then we uh import a single image

    from MNEST data set which is handwritten from MNEST data set which is handwritten
    from MNEST data set which is handwritten

    digits. >> [snorts]

    >> Okay. Now what we do is we define the >> Okay. Now what we do is we define
    the >> Okay. Now what we do is we define the

    noise schedule for the forward diffusion noise schedule for the forward diffusion
    noise schedule for the forward diffusion

    process. We have already looked at this process. We have already looked at this
    process. We have already looked at this

    and uh we do the forward diffusion and uh we do the forward diffusion and uh we
    do the forward diffusion

    first. So you can see how it goes from first. So you can see how it goes from
    first. So you can see how it goes from

    the original image to the final image in the original image to the final image
    in'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 73
  start_sec: 4487.36
  end_sec: 4548.48
  text: 'the original image to the final image in

    100 steps. We have already seen how to 100 steps. We have already seen how to
    100 steps. We have already seen how to

    uh write down this forward diffusion uh write down this forward diffusion uh write
    down this forward diffusion

    equation in the previous in in this equation in the previous in in this equation
    in the previous in in this

    example. The main thing here is how to get the The main thing here is how to get
    the

    true posterior how to get the mean and true posterior how to get the mean and
    true posterior how to get the mean and

    the variance for the true reverse the variance for the true reverse the variance
    for the true reverse

    process. process. process.

    And for that let''s try to unpack this. And for that let''s try to unpack this.
    And for that let''s try to unpack this.

    Okay. So here you see first we calculate Okay. So here you see first we calculate
    Okay. So here you see first we calculate

    coefficient one which is coefficient one which is coefficient one which is

    uh a1 in this case and next we calculate uh a1 in this case and next we calculate
    uh a1 in this case and next we calculate

    coefficient 2 which is coefficient 2 which is coefficient 2 which is

    a2 in this case and then we do a2 in this case and then we do a2 in this case
    and then we do

    coefficient 1 into x0 plus coefficient 2 coefficient 1 into x0 plus coefficient
    2 coefficient 1 into x0 plus coefficient 2

    into x i which is exactly what is given into x i which is exactly what is given
    into x i which is exactly what is given

    over here over here over here

    and the variance is given by a3 which is and the variance is given by a3 which
    is and the variance is given by a3 which is

    mentioned here. Now exactly how these mentioned here. Now exactly how these mentioned
    here. Now exactly how these

    coefficients are calculated, it is a coefficients are calculated, it is a coefficients
    are calculated, it is a

    function of function of function of

    alphas and betas which is mentioned in alphas and betas which is mentioned in'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 74
  start_sec: 4548.48
  end_sec: 4613.35
  text: 'alphas and betas which is mentioned in

    the paper. So I have deliberately stayed the paper. So I have deliberately stayed
    the paper. So I have deliberately stayed

    away from it. I don''t want to get too away from it. I don''t want to get too
    away from it. I don''t want to get too

    too mathematical uh in in this part. All too mathematical uh in in this part.
    All too mathematical uh in in this part. All

    I want you to understand is that I want you to understand is that I want you to
    understand is that

    coefficient one only depend on whatever coefficient one only depend on whatever
    coefficient one only depend on whatever

    parameters you have used in the forward parameters you have used in the forward
    parameters you have used in the forward

    process [snorts] which you already know process [snorts] which you already know
    process [snorts] which you already know

    in in in hand. So you can easily in in in hand. So you can easily in in in hand.
    So you can easily

    calculate this and then once that is calculate this and then once that is calculate
    this and then once that is

    done you can actually visualize done you can actually visualize done you can actually
    visualize

    how you go from uh okay so maybe I did how you go from uh okay so maybe I did
    how you go from uh okay so maybe I did

    not run this. not run this. not run this.

    Yeah, let''s let''s run this. Yeah, let''s let''s run this. Yeah, let''s let''s
    run this.

    Okay, so now what you do is you start Okay, so now what you do is you start Okay,
    so now what you do is you start

    from uh from uh from uh

    very high noise very high noise very high noise

    and what you do is you end with and what you do is you end with and what you do
    is you end with

    okay you remove noise and you end over okay you remove noise and you end over
    okay you remove noise and you end over

    here. So you start from step 50 you go here. So you start from step 50 you go
    here. So you start from step 50 you go

    to 49 48 47 and finally you move to'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 75
  start_sec: 4613.35
  end_sec: 4665.28
  text: 'to 49 48 47 and finally you move to to 49 48 47 and finally you move to

    the original image. So, so it actually the original image. So, so it actually
    the original image. So, so it actually

    works right you you you go from noise works right you you you go from noise works
    right you you you go from noise

    and you remove noise in a progressive and you remove noise in a progressive and
    you remove noise in a progressive

    way and you reach the original image. way and you reach the original image. way
    and you reach the original image.

    So, uh the the true posterior for the So, uh the the true posterior for the So,
    uh the the true posterior for the

    reverse transition actually works. This reverse transition actually works. This
    reverse transition actually works. This

    is what we saw in this Google collab is what we saw in this Google collab is what
    we saw in this Google collab

    demo. demo. demo.

    One interesting point which I really One interesting point which I really One
    interesting point which I really

    want to mention here is that want to mention here is that want to mention here
    is that

    uh you see here in the forward diffusion uh you see here in the forward diffusion
    uh you see here in the forward diffusion

    process we have used this formula alpha process we have used this formula alpha
    process we have used this formula alpha

    squar + beta square is equal to 1. squar + beta square is equal to 1. squar +
    beta square is equal to 1.

    Whereas here Whereas here Whereas here

    we have done alpha + beta is equal to 1. we have done alpha + beta is equal to
    1. we have done alpha + beta is equal to 1.

    And somehow this is a standard norm. I And somehow this is a standard norm. I
    And somehow this is a standard norm. I

    have seen this in a lot of uh codes have seen this in a lot of uh codes have seen
    this in a lot of uh codes

    where people use diffusion and upload where people use diffusion and upload where
    people use diffusion and upload

    their codes on GitHub. their codes on GitHub.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 76
  start_sec: 4665.28
  end_sec: 4717.99
  text: 'their codes on GitHub.

    So this alpha actually represents alpha So this alpha actually represents alpha
    So this alpha actually represents alpha

    square in our notation and this beta square in our notation and this beta square
    in our notation and this beta

    actually represents beta square. actually represents beta square. actually represents
    beta square.

    So people basically So people basically So people basically

    don''t like to use alpha square and beta don''t like to use alpha square and beta
    don''t like to use alpha square and beta

    square separately like we do over here. square separately like we do over here.
    square separately like we do over here.

    But they define one notation for or one But they define one notation for or one
    But they define one notation for or one

    single symbol for alpha square which single symbol for alpha square which single
    symbol for alpha square which

    they call as alpha and one single symbol they call as alpha and one single symbol
    they call as alpha and one single symbol

    for beta square which they call as beta. for beta square which they call as beta.
    for beta square which they call as beta.

    So it is just a change in the notation. So it is just a change in the notation.
    So it is just a change in the notation.

    Everything else really stays the same. Everything else really stays the same.
    Everything else really stays the same.

    So I I wanted you to be aware of this so So I I wanted you to be aware of this
    so So I I wanted you to be aware of this so

    that whenever you encounter codes where that whenever you encounter codes where
    that whenever you encounter codes where

    noise schedule is defined and you see oh noise schedule is defined and you see
    oh noise schedule is defined and you see oh

    why is this alpha plus beta equal to 1. why is this alpha plus beta equal to 1.
    why is this alpha plus beta equal to 1.

    I have learned that alpha square plus I have learned that alpha square plus I
    have learned that alpha square plus

    beta square equal to 1. It''s because beta square equal to 1. It''s because beta
    square equal to 1. It''s because

    this beta is it it represents beta'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 77
  start_sec: 4717.99
  end_sec: 4768.229
  text: 'this beta is it it represents beta this beta is it it represents beta

    square which is the variance in our square which is the variance in our square
    which is the variance in our

    notation and alpha represents alpha notation and alpha represents alpha notation
    and alpha represents alpha

    square in our notation. So it''s just a square in our notation. So it''s just
    a square in our notation. So it''s just a

    change of notation which people usually change of notation which people usually
    change of notation which people usually

    find convenient and that''s why they go find convenient and that''s why they go
    find convenient and that''s why they go

    ahead with this. Just just practice with ahead with this. Just just practice with
    ahead with this. Just just practice with

    this a little bit so that you''ll get this a little bit so that you''ll get this
    a little bit so that you''ll get

    familiar with the notation and uh why it familiar with the notation and uh why
    it familiar with the notation and uh why it

    is used. Okay. So now we know that the reverse Okay. So now we know that the reverse

    transition can also be represented as a transition can also be represented as
    a transition can also be represented as a

    wash which helps us a lot. So what we can do which helps us a lot. So what we
    can do

    now is now is now is

    a thought might come to your mind which a thought might come to your mind which
    a thought might come to your mind which

    says that we know the entire reverse says that we know the entire reverse says
    that we know the entire reverse

    process. So are we done? process. So are we done? process. So are we done?

    Not quite. The reason is that we have Not quite. The reason is that we have Not
    quite. The reason is that we have

    calculated the reverse transition kernel calculated the reverse transition kernel
    calculated the reverse transition kernel

    conditioned on the original image. But conditioned on the original image. But
    conditioned on the original image. But

    in the application we have to generate in the application we have to generate
    in the application we have to generate

    the image from noise. So the original'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 78
  start_sec: 4768.229
  end_sec: 4832.719
  text: 'the image from noise. So the original the image from noise. So the original

    image will not be given to us. image will not be given to us. image will not be
    given to us.

    So basically we want to uh predict this So basically we want to uh predict this
    So basically we want to uh predict this

    predict uh this distribution which is predict uh this distribution which is predict
    uh this distribution which is

    predicted by our decoder and you can see predicted by our decoder and you can
    see predicted by our decoder and you can see

    there is no original image given over there is no original image given over there
    is no original image given over

    here but [clears throat] this is here but [clears throat] this is here but [clears
    throat] this is

    something which we already know. something which we already know. something which
    we already know.

    So uh So uh

    people assume that since the people assume that since the people assume that since
    the

    is what we want to learn and our model is what we want to learn and our model
    is what we want to learn and our model

    wants to approximate this we use the wants to approximate this we use the wants
    to approximate this we use the

    same variance same variance same variance

    but the mean has to be predicted. but the mean has to be predicted. but the mean
    has to be predicted.

    So the first assumption is that our So the first assumption is that our So the
    first assumption is that our

    reverse transition kernel which our reverse transition kernel which our reverse
    transition kernel which our

    neural network predicts neural network predicts neural network predicts

    that also is a gshian which is I think a that also is a gshian which is I think
    a that also is a gshian which is I think a

    major assumption. And the second major assumption. And the second major assumption.
    And the second

    assumption is that the variance stays assumption is that the variance stays assumption
    is that the variance stays

    the same. The only component which we the same. The only component which we the
    same. The only component which we

    have to predict is the mean. Okay. So now we have two gshian'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 79
  start_sec: 4832.719
  end_sec: 4888.321
  text: 'Okay. So now we have two gshian

    distributions. First goshian distributions. First goshian distributions. First
    goshian

    distribution we know the mean and distribution we know the mean and distribution
    we know the mean and

    variance. second gshian distribution the variance. second gshian distribution
    the variance. second gshian distribution the

    variance is the same but the only variance is the same but the only variance is
    the same but the only

    difference is that the mean has to be difference is that the mean has to be difference
    is that the mean has to be

    predicted. predicted. predicted.

    So it turns out that So it turns out that So it turns out that

    minimizing the k divergence between two minimizing the k divergence between two
    minimizing the k divergence between two

    gshians with the same variation gshians with the same variation gshians with the
    same variation

    is is very simple. So basically these is is very simple. So basically these is
    is very simple. So basically these

    are the two gshians with the same are the two gshians with the same are the two
    gshians with the same

    variance but the means are located at variance but the means are located at variance
    but the means are located at

    different positions right. different positions right. different positions right.

    So [clears throat] So [clears throat] So [clears throat]

    the kale divergence can simply be the kale divergence can simply be the kale divergence
    can simply be

    written as written as written as

    some factor multiplied by the squared some factor multiplied by the squared some
    factor multiplied by the squared

    difference of the means. difference of the means. difference of the means.

    So this is quite easy right? So all we So this is quite easy right? So all we
    So this is quite easy right? So all we

    have to do is we have to make sure the have to do is we have to make sure the
    have to do is we have to make sure the

    mean of this our our predicted version mean of this our our predicted version
    mean of this our our predicted version

    lies as close as possible to this mean lies as close as possible to this mean
    lies as close as possible to this mean

    which we have predicted over here. which we have predicted over here.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 80
  start_sec: 4888.321
  end_sec: 4943.28
  text: 'which we have predicted over here.

    >> [snorts] >> [snorts]

    >> So now it boils down to a simple uh >> So now it boils down to a simple uh
    >> So now it boils down to a simple uh

    algebraic manipulation. So algebraic manipulation. So algebraic manipulation.
    So

    okay so this is this is something we okay so this is this is something we okay
    so this is this is something we

    know uh we know that this is our mean of know uh we know that this is our mean
    of know uh we know that this is our mean of

    u u u

    the true posterior which we know a1 and the true posterior which we know a1 and
    the true posterior which we know a1 and

    a2 we already know. Now what we do is we a2 we already know. Now what we do is
    we a2 we already know. Now what we do is we

    use a exact same structure for the mean use a exact same structure for the mean
    use a exact same structure for the mean

    of our model. of our model. of our model.

    We use the same A2 because the We use the same A2 because the We use the same
    A2 because the

    uh standard deviation is is is the same uh standard deviation is is is the same
    uh standard deviation is is is the same

    and we use same A1 also. The the only and we use same A1 also. The the only and
    we use same A1 also. The the only

    difference is that we use X0 not here difference is that we use X0 not here difference
    is that we use X0 not here

    because we don''t have access to the true because we don''t have access to the
    true because we don''t have access to the true

    image. So our mean is going to be image. So our mean is going to be image. So
    our mean is going to be

    predicted based on a predicted true predicted based on a predicted true predicted
    based on a predicted true

    image image image

    which is which is something we don''t which is which is something we don''t which
    is which is something we don''t

    really know. And now if you apply this really know. And now if you apply this'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 81
  start_sec: 4943.28
  end_sec: 5018.0
  text: 'really know. And now if you apply this

    formula mu of 5 - mu² formula mu of 5 - mu² formula mu of 5 - mu²

    what you see is you want to basically what you see is you want to basically what
    you see is you want to basically

    minimize this x0 hat - x0 square. x0 hat - x0 square.

    Now this is a bit illuminating. What Now this is a bit illuminating. What Now
    this is a bit illuminating. What

    what does this mean? What what are we what does this mean? What what are we what
    does this mean? What what are we

    trying to do over here? trying to do over here? trying to do over here?

    What we are trying to do over here is What we are trying to do over here is What
    we are trying to do over here is

    let''s say in the true data we have uh we let''s say in the true data we have
    uh we let''s say in the true data we have uh we

    have Batman have Batman have Batman

    okay and then in the reverse process we okay and then in the reverse process we
    okay and then in the reverse process we

    are just given noise. are just given noise. are just given noise.

    So what I''m essentially saying is that So what I''m essentially saying is that
    So what I''m essentially saying is that

    for my neural network to work properly, for my neural network to work properly,
    for my neural network to work properly,

    I need to find an estimate of the true I need to find an estimate of the true
    I need to find an estimate of the true

    image which is as close as possible to image which is as close as possible to
    image which is as close as possible to

    this image. And uh And uh

    that is something which is quite that is something which is quite that is something
    which is quite

    intuitive, right? Because if you if you intuitive, right? Because if you if you
    intuitive, right? Because if you if you

    had the prediction of the true image had the prediction of the true image had
    the prediction of the true image

    correct then then

    uh the reverse transition process will uh the reverse transition process will'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 82
  start_sec: 5018.0
  end_sec: 5072.87
  text: 'uh the reverse transition process will

    be same as that of the true posterior be same as that of the true posterior be
    same as that of the true posterior

    because then you have the same because then you have the same because then you
    have the same

    information which the true posterior information which the true posterior information
    which the true posterior

    has. has. has.

    But then this is not we we don''t know But then this is not we we don''t know
    But then this is not we we don''t know

    what this is. So that''s why we want to what this is. So that''s why we want to
    what this is. So that''s why we want to

    predict this and we want to make it as predict this and we want to make it as
    predict this and we want to make it as

    close as possible to for example the close as possible to for example the close
    as possible to for example the

    image of a Batman in that case. But if image of a Batman in that case. But if
    image of a Batman in that case. But if

    it turns out that X0 hat is the image of it turns out that X0 hat is the image
    of it turns out that X0 hat is the image of

    let''s say Spider-Man then this let''s say Spider-Man then this let''s say Spider-Man
    then this

    difference will be huge. difference will be huge. difference will be huge.

    But people go one step further and uh we But people go one step further and uh
    we But people go one step further and uh we

    will come to a very compact and will come to a very compact and will come to a
    very compact and

    beautiful expression at the end. beautiful expression at the end. beautiful expression
    at the end.

    So one thing we know is that So one thing we know is that So one thing we know
    is that

    uh x i which is the image at any time uh x i which is the image at any time uh
    x i which is the image at any time

    step in the forward process step in the forward process step in the forward process

    it can be written as a function of the'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 83
  start_sec: 5072.87
  end_sec: 5134.239
  text: 'it can be written as a function of the it can be written as a function of
    the

    original image original image original image

    and noise. and noise. and noise.

    Remember this was the homework which I Remember this was the homework which I
    Remember this was the homework which I

    gave you. How can we go from the gave you. How can we go from the gave you. How
    can we go from the

    original image to any single image in original image to any single image in original
    image to any single image in

    the forward transition process? And uh the forward transition process? And uh
    the forward transition process? And uh

    it it turns out that the cumulative it it turns out that the cumulative it it
    turns out that the cumulative

    alpha I bar is just the multiplication alpha I bar is just the multiplication
    alpha I bar is just the multiplication

    of all all alphas alpha 1 into alpha 2 of all all alphas alpha 1 into alpha 2
    of all all alphas alpha 1 into alpha 2

    into alpha 3 etc. into alpha 3 etc. into alpha 3 etc.

    And And

    the cumulative beta is just root of 1 the cumulative beta is just root of 1 the
    cumulative beta is just root of 1

    minus alpha bar square since the square minus alpha bar square since the square
    minus alpha bar square since the square

    of this should add up to one. of this should add up to one. of this should add
    up to one.

    So this is a formula which takes us from So this is a formula which takes us from
    So this is a formula which takes us from

    the original image to any single image the original image to any single image
    the original image to any single image

    in the transition. in the transition. in the transition.

    And here epsilon is the noise that we And here epsilon is the noise that we And
    here epsilon is the noise that we

    are adding in the forward process. are adding in the forward process. are adding
    in the forward process.

    And this should also be I actually And this should also be I actually And this
    should also be I actually

    because the noise depends on uh how much noise we are basically'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 84
  start_sec: 5134.239
  end_sec: 5215.92
  text: 'uh how much noise we are basically

    adding at each step. adding at each step. adding at each step.

    Okay. So uh but for now let''s let''s keep Okay. So uh but for now let''s let''s
    keep Okay. So uh but for now let''s let''s keep

    it just epsilon. So we can substitute x0 it just epsilon. So we can substitute
    x0 it just epsilon. So we can substitute x0

    with this because we can just write x0 as x i because we can just write x0 as
    x i

    minus this term divided by alpha i bar minus this term divided by alpha i bar
    minus this term divided by alpha i bar

    and this can be written as some number and this can be written as some number
    and this can be written as some number

    into x i minus some number into noise. into x i minus some number into noise.
    into x i minus some number into noise.

    So this is the noise which is uh added So this is the noise which is uh added
    So this is the noise which is uh added

    in the forward diffusion process. So what this means is that So what this means
    is that

    you can write the true image as you can write the true image as you can write
    the true image as

    given any image in the forward process given any image in the forward process
    given any image in the forward process

    but just subtract it with appropriate but just subtract it with appropriate but
    just subtract it with appropriate

    noise. noise. noise.

    So for example, this means that So for example, this means that So for example,
    this means that

    if if if

    this is x0, right? So if I want to go this is x0, right? So if I want to go this
    is x0, right? So if I want to go

    from x3 to x0, I just have to reduce from x3 to x0, I just have to reduce from
    x3 to x0, I just have to reduce

    noise in a very specific way from each noise in a very specific way from each
    noise in a very specific way from each

    of the pixels in in this image. So So this is what this means. So x0 can'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 85
  start_sec: 5215.92
  end_sec: 5273.03
  text: 'So So this is what this means. So x0 can

    in fact be written in as in in this way. in fact be written in as in in this way.
    in fact be written in as in in this way.

    And in the paper what they do is since And in the paper what they do is since
    And in the paper what they do is since

    we do not know x0 hat we also write this we do not know x0 hat we also write this
    we do not know x0 hat we also write this

    in a very similar way in a very similar way in a very similar way

    as a function of x i c1 * x i minus c2 * as a function of x i c1 * x i minus c2
    * as a function of x i c1 * x i minus c2 *

    epsilon hat which is the noise which is epsilon hat which is the noise which is
    epsilon hat which is the noise which is

    predicted by our neural network. predicted by our neural network. predicted by
    our neural network.

    Now we do not know this noise beforehand Now we do not know this noise beforehand
    Now we do not know this noise beforehand

    but let us try to substitute this in the but let us try to substitute this in
    the but let us try to substitute this in the

    original equation and then see what we original equation and then see what we
    original equation and then see what we

    get. So [snorts] what we get is the get. So [snorts] what we get is the get. So
    [snorts] what we get is the

    scaled. So finally what we want to scaled. So finally what we want to scaled.
    So finally what we want to

    minimize is x0 hat - x0 square which is minimize is x0 hat - x0 square which is
    minimize is x0 hat - x0 square which is

    epsilon minus epsilon hat square. epsilon minus epsilon hat square. epsilon minus
    epsilon hat square.

    And this yields the final loss function And this yields the final loss function
    And this yields the final loss function

    which is over here. which is over here. which is over here.

    >> [snorts] >> [snorts]

    >> Now you see the uh simplicity of this.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 86
  start_sec: 5273.03
  end_sec: 5331.76
  text: '>> Now you see the uh simplicity of this. >> Now you see the uh simplicity
    of this.

    What this essentially means is that What this essentially means is that What this
    essentially means is that

    what I need to do is in my reverse what I need to do is in my reverse what I need
    to do is in my reverse

    process I need to predict how much noise process I need to predict how much noise
    process I need to predict how much noise

    do I need to subtract do I need to subtract do I need to subtract

    at each point in the transition at each point in the transition at each point
    in the transition

    such that this noise such that this noise such that this noise

    matches as close as possible to the true matches as close as possible to the true
    matches as close as possible to the true

    noise which is added at each time step. noise which is added at each time step.
    noise which is added at each time step.

    So what this means is like uh if if So what this means is like uh if if So what
    this means is like uh if if

    let''s say in the forward process we are let''s say in the forward process we
    are let''s say in the forward process we are

    adding certain noise right to every adding certain noise right to every adding
    certain noise right to every

    single image in the reverse process our single image in the reverse process our
    single image in the reverse process our

    objective is to predict that noise we objective is to predict that noise we objective
    is to predict that noise we

    want to find how much noise is added in want to find how much noise is added in
    want to find how much noise is added in

    the forward process the forward process the forward process

    and that is what the reverse transition and that is what the reverse transition
    and that is what the reverse transition

    kernel prediction boils down to. kernel prediction boils down to. kernel prediction
    boils down to.

    We want to predict the noise level that We want to predict the noise level that
    We want to predict the noise level that

    we have imparted at each transition. we have imparted at each transition.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 87
  start_sec: 5331.76
  end_sec: 5409.52
  text: 'we have imparted at each transition.

    Once we have this noise level, we can Once we have this noise level, we can Once
    we have this noise level, we can

    actually calculate the the the images at every single the the the images at every
    single

    transition using this formula. But what we ideally want is to at every But what
    we ideally want is to at every

    single step we need to find how much single step we need to find how much single
    step we need to find how much

    noise has noise has noise has

    my model added in the forward process my model added in the forward process my
    model added in the forward process

    and my neural network has to learn that and my neural network has to learn that
    and my neural network has to learn that

    without having any information of the without having any information of the without
    having any information of the

    true image. true image. true image.

    So this is this is exactly what happens So this is this is exactly what happens
    So this is this is exactly what happens

    in the reverse diffusion process and if in the reverse diffusion process and if
    in the reverse diffusion process and if

    you look at their paper you look at their paper you look at their paper

    it appears slightly mathematically it appears slightly mathematically it appears
    slightly mathematically

    intensive but whatever I have included intensive but whatever I have included
    intensive but whatever I have included

    is the same thing and is the same thing and is the same thing and

    here basically they say exactly the same here basically they say exactly the same
    here basically they say exactly the same

    thing where in the training process thing where in the training process thing
    where in the training process

    we are trying to uh let''s try to see if we are trying to uh let''s try to see
    if we are trying to uh let''s try to see if

    we can uh find any wording here which we can uh find any wording here which we
    can uh find any wording here which

    makes sense. So this is the final makes sense. So this is the final makes sense.
    So this is the final

    equation which which they get equation which which they get'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 88
  start_sec: 5409.52
  end_sec: 5477.75
  text: 'equation which which they get

    uh you know and here you see we finally uh you know and here you see we finally
    uh you know and here you see we finally

    have epsilon minus epsilon theta whole have epsilon minus epsilon theta whole
    have epsilon minus epsilon theta whole

    square square square

    which means that we are trying to which means that we are trying to which means
    that we are trying to

    minimize noise from the true noise and e minimize noise from the true noise and
    e minimize noise from the true noise and e

    theta is a function approximator theta is a function approximator theta is a function
    approximator

    intended to predict epsilon from xt. Okay. So uh this is exactly what is the Okay.
    So uh this is exactly what is the

    final outcome of this paper. I I really final outcome of this paper. I I really
    final outcome of this paper. I I really

    want all of you to go through this paper want all of you to go through this paper
    want all of you to go through this paper

    step by step. I strongly think you will step by step. I strongly think you will
    step by step. I strongly think you will

    understand most of the things which are understand most of the things which are
    understand most of the things which are

    mentioned in this paper and some of the mentioned in this paper and some of the
    mentioned in this paper and some of the

    concepts related to score matching. I do concepts related to score matching. I
    do concepts related to score matching. I do

    not expect you to understand but I not expect you to understand but I not expect
    you to understand but I

    expect you to understand some of the expect you to understand some of the expect
    you to understand some of the

    main uh contributions main uh contributions main uh contributions

    of this paper. of this paper. of this paper.

    And uh And uh

    if if you understand the intuitions if if you understand the intuitions if if
    you understand the intuitions

    behind uh these contributions, behind uh these contributions, behind uh these
    contributions,

    you will really begin to appreciate you will really begin to appreciate you will
    really begin to appreciate

    diffusion models and and why they work.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 89
  start_sec: 5477.75
  end_sec: 5533.28
  text: 'diffusion models and and why they work. diffusion models and and why they
    work.

    So uh please take a print out and go So uh please take a print out and go So uh
    please take a print out and go

    through all these different aspects in through all these different aspects in
    through all these different aspects in

    detail so that you''re familiar with the detail so that you''re familiar with
    the detail so that you''re familiar with the

    concepts in in depth. concepts in in depth. concepts in in depth.

    So let me quickly revise what we learned So let me quickly revise what we learned
    So let me quickly revise what we learned

    in this process. So we had uh in this process. So we had uh in this process. So
    we had uh

    the variational autoenccoders to start the variational autoenccoders to start
    the variational autoenccoders to start

    with and we wanted to use a similar with and we wanted to use a similar with and
    we wanted to use a similar

    framework but we started out with framework but we started out with framework
    but we started out with

    replacing the encoder with a diffuser replacing the encoder with a diffuser replacing
    the encoder with a diffuser

    with two simple properties that the with two simple properties that the with two
    simple properties that the

    structure should disappear and it should structure should disappear and it should
    structure should disappear and it should

    become uniform. And we wanted to fix the become uniform. And we wanted to fix
    the become uniform. And we wanted to fix the

    encoder. In VA the encoder and decoder encoder. In VA the encoder and decoder
    encoder. In VA the encoder and decoder

    are trained separately but in this case are trained separately but in this case
    are trained separately but in this case

    we wanted to fix the encoder. So we only we wanted to fix the encoder. So we only
    we wanted to fix the encoder. So we only

    need to train the decoder. need to train the decoder. need to train the decoder.

    So first step is is that we define the So first step is is that we define the
    So first step is is that we define the

    encoder as a goshian transition kernel encoder as a goshian transition kernel'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 90
  start_sec: 5533.28
  end_sec: 5585.44
  text: 'encoder as a goshian transition kernel

    with a specific mean and variance. And with a specific mean and variance. And
    with a specific mean and variance. And

    we have different iterations which go we have different iterations which go we
    have different iterations which go

    from image to noise. We don''t do it one from image to noise. We don''t do it
    one from image to noise. We don''t do it one

    single shot. we have 100 steps in single shot. we have 100 steps in single shot.
    we have 100 steps in

    between or multiple steps in between and between or multiple steps in between
    and between or multiple steps in between and

    every single step you add noise. every single step you add noise. every single
    step you add noise.

    So this is the forward process which we So this is the forward process which we
    So this is the forward process which we

    exactly know. Now the objective is how exactly know. Now the objective is how
    exactly know. Now the objective is how

    can we find the reverse process? How can can we find the reverse process? How
    can can we find the reverse process? How can

    we generate data from noise? And it we generate data from noise? And it we generate
    data from noise? And it

    turns out that the objective in the turns out that the objective in the turns
    out that the objective in the

    reverse process is to finally maximize reverse process is to finally maximize
    reverse process is to finally maximize

    the likelihood of the data which is the likelihood of the data which is the likelihood
    of the data which is

    sampled from the real distribution and sampled from the real distribution and
    sampled from the real distribution and

    using a bit of mathematics it turns out using a bit of mathematics it turns out
    using a bit of mathematics it turns out

    that it''s a function of reconstruction that it''s a function of reconstruction
    that it''s a function of reconstruction

    term regularization term and matching term regularization term and matching term
    regularization term and matching

    the reverse transition kernel. Now the the reverse transition kernel. Now the
    the reverse transition kernel. Now the

    first two terms are exactly same like we first two terms are exactly same like
    we'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 91
  start_sec: 5585.44
  end_sec: 5634.88
  text: 'first two terms are exactly same like we

    saw in VAS. The regularization term is saw in VAS. The regularization term is
    saw in VAS. The regularization term is

    not important here because we already not important here because we already not
    important here because we already

    have noise in the encoder uh in the have noise in the encoder uh in the have noise
    in the encoder uh in the

    encoding process. Reconstruction term is encoding process. Reconstruction term
    is encoding process. Reconstruction term is

    something which people usually neglect something which people usually neglect
    something which people usually neglect

    and the only term they focus on is the and the only term they focus on is the
    and the only term they focus on is the

    third term is to make sure that the third term is to make sure that the third
    term is to make sure that the

    reverse transition kernel which our reverse transition kernel which our

    neural network predicts it matches as neural network predicts it matches as neural
    network predicts it matches as

    close as possible to the true posterior. close as possible to the true posterior.
    close as possible to the true posterior.

    Now we just wanted to appreciate the Now we just wanted to appreciate the Now
    we just wanted to appreciate the

    structure of this true posterior which structure of this true posterior which
    structure of this true posterior which

    is conditioned on the original data. If is conditioned on the original data. If
    is conditioned on the original data. If

    we just wanted to predict the image we just wanted to predict the image we just
    wanted to predict the image

    which comes before the current time which comes before the current time which
    comes before the current time

    step, it''s very hard. But if it is step, it''s very hard. But if it is step,
    it''s very hard. But if it is

    conditioned on the original data, it conditioned on the original data, it conditioned
    on the original data, it

    suddenly becomes easier. suddenly becomes easier. suddenly becomes easier.

    This allowed us to calculate the true This allowed us to calculate the true This
    allowed us to calculate the true

    posterior in a very tractable way. And posterior in a very tractable way. And'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 92
  start_sec: 5634.88
  end_sec: 5682.4
  text: 'posterior in a very tractable way. And

    we saw that it can be written as a we saw that it can be written as a we saw that
    it can be written as a

    gshian with a mean and a variance. The gshian with a mean and a variance. The
    gshian with a mean and a variance. The

    mean depends on the current image and mean depends on the current image and mean
    depends on the current image and

    the original image. the original image.

    So we know the true posterior and we So we know the true posterior and we So we
    know the true posterior and we

    want our reverse transition kernel which want our reverse transition kernel which
    want our reverse transition kernel which

    our model predicts to match this true our model predicts to match this true our
    model predicts to match this true

    transition. This this true posterior. transition. This this true posterior. transition.
    This this true posterior.

    So we assume that our model prediction So we assume that our model prediction
    So we assume that our model prediction

    is also gshian with a mean and a is also gshian with a mean and a is also gshian
    with a mean and a

    variance which is exactly the same as variance which is exactly the same as variance
    which is exactly the same as

    the true posterior. So it turns out that the true posterior. So it turns out that
    the true posterior. So it turns out that

    if you want to minimize the KL if you want to minimize the KL if you want to minimize
    the KL

    divergence between two distributions, divergence between two distributions, divergence
    between two distributions,

    two gshian distributions having the same two gshian distributions having the same
    two gshian distributions having the same

    variance, we just have to make sure variance, we just have to make sure variance,
    we just have to make sure

    their means are close to each other. their means are close to each other. their
    means are close to each other.

    And then after we distill this even And then after we distill this even And then
    after we distill this even

    more, we we found out that at the heart more, we we found out that at the heart'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 93
  start_sec: 5682.4
  end_sec: 5740.39
  text: 'more, we we found out that at the heart

    of it, we want to make sure that the of it, we want to make sure that the of it,
    we want to make sure that the

    original image true data which original image true data which original image true
    data which

    our reverse transition model predicts at our reverse transition model predicts
    at our reverse transition model predicts at

    the last time step is as close as the last time step is as close as the last time
    step is as close as

    possible to the actual true data. possible to the actual true data. possible to
    the actual true data.

    And we further simplify it and boil it And we further simplify it and boil it
    And we further simplify it and boil it

    down to a notation which only includes down to a notation which only includes
    down to a notation which only includes

    noise. noise.

    So we say that at the end what we are So we say that at the end what we are So
    we say that at the end what we are

    trying to do is we are trying to find trying to do is we are trying to find trying
    to do is we are trying to find

    out the reverse transition neural out the reverse transition neural out the reverse
    transition neural

    network such that it predicts noise at network such that it predicts noise at
    network such that it predicts noise at

    every single time step every single time step every single time step

    and this noise is going to be a function and this noise is going to be a function
    and this noise is going to be a function

    of of of

    uh the current image as well as the time uh the current image as well as the time
    uh the current image as well as the time

    step that you are looking at. But this step that you are looking at. But this
    step that you are looking at. But this

    noise has to match as close as possible noise has to match as close as possible
    noise has to match as close as possible

    to the true noise which has been added to the true noise which has been added
    to the true noise which has been added

    in the forward diffusion process.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 94
  start_sec: 5740.39
  end_sec: 5786.239
  text: 'in the forward diffusion process. in the forward diffusion process.

    And this this makes a lot of sense. And this this makes a lot of sense. And this
    this makes a lot of sense.

    That''s why the name dinoising comes in That''s why the name dinoising comes in
    That''s why the name dinoising comes in

    this paper. We are finally learning how this paper. We are finally learning how
    this paper. We are finally learning how

    to d noiseise to d noiseise to d noiseise

    how to subtract noise from the images. how to subtract noise from the images.
    how to subtract noise from the images.

    This is what we are trying to learn in This is what we are trying to learn in
    This is what we are trying to learn in

    this whole process. this whole process. this whole process.

    And [snorts] you understand why the word And [snorts] you understand why the word
    And [snorts] you understand why the word

    diffusion now comes. The reason these diffusion now comes. The reason these diffusion
    now comes. The reason these

    are called probabilistic models is is is are called probabilistic models is is
    is are called probabilistic models is is is

    something we have learned from the something we have learned from the something
    we have learned from the

    beginning of deep generative models. Our beginning of deep generative models.
    Our beginning of deep generative models. Our

    objective is to learn a distribution objective is to learn a distribution objective
    is to learn a distribution

    here of the data. So that''s why the name here of the data. So that''s why the
    name here of the data. So that''s why the name

    probabilistic models comes into the probabilistic models comes into the probabilistic
    models comes into the

    picture. picture. picture.

    At the end I really want you to take a At the end I really want you to take a
    At the end I really want you to take a

    print out and read this paper and uh print out and read this paper and uh print
    out and read this paper and uh

    share your findings. If you find share your findings. If you find share your findings.
    If you find

    something which is more insightful, something which is more insightful, something
    which is more insightful,

    please let me know please let me know'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
- idx: 95
  start_sec: 5786.239
  end_sec: 5807.4
  text: 'please let me know

    and just just sit down and go through and just just sit down and go through and
    just just sit down and go through

    this homework problem where you find the this homework problem where you find
    the this homework problem where you find the

    mean and the variance mean and the variance mean and the variance

    if we go directly from the original if we go directly from the original if we
    go directly from the original

    image to any single time step in this image to any single time step in this image
    to any single time step in this

    forward transition. Thank you very much forward transition. Thank you very much
    forward transition. Thank you very much

    everyone and uh in the next lecture we everyone and uh in the next lecture we
    everyone and uh in the next lecture we

    will cover a practical example of this will cover a practical example of this
    will cover a practical example of this

    diffusion process. Thank you.'
  concept_slugs:
  - ddpm
  - forward-process
  - reverse-process
---
# Lecture 3 - Introduction to Diffusion Models (DDPM) | Principles of Diffusion Models

See the structured chunks above.
