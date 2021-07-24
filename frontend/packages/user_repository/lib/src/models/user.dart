class User {
  final int pk;
  final String email;
  final String firstName;
  final String lastName;

  const User({
    required this.pk,
    required this.email,
    required this.firstName,
    required this.lastName,
  });

  static const anonymous = User(
    pk: 0,
    email: '',
    firstName: '',
    lastName: '',
  );
}
