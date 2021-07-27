import 'package:flutter/material.dart';

class AnnouncementsPage extends StatelessWidget {
  const AnnouncementsPage({Key? key}) : super(key: key);

  static Page page() => const MaterialPage<void>(child: AnnouncementsPage());

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text('Announcements Page'),
    );
  }
}
