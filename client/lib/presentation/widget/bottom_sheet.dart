import 'package:flutter/material.dart';

class BottomSheetWidget extends StatelessWidget {
  final String text;
  final VoidCallback onPressed;
  final Color color;

  const BottomSheetWidget({
    super.key,
    required this.text,
    required this.onPressed,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Container(color: color, child: Text(text));
  }
}
